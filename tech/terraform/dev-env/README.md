This is my attempt at using terraform to setup a basic dev environment in aws.

Attempting to setup a VPC with: 
1) public security group
2) public subnet
3) EC2 in that public subnet
4) Public route table to control trffic to the public subnet
5) Internet Gateway to allow external traffic to the route table/public subnet 

Steps: 
* initialize terraform 
``` 
-> terraform init
```
* configure aws
```
// providers.tf

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
    region = "us-east-1"
    shared_credentials_files = ["C:\\Users\\oogabooga\\.aws\\credentials"]
    profile = "VsCode-Terraform"
}
```
* create vpc
```
// main.tf
resource "aws_default_vpc" "default-vpc {
  tags = {
    Name = "Default VPC"
  }
}

--> terraform plan
--> terraform apply
```
* create subnet
```
// main.tf  

resource "aws_subnet" "main_public_subnet" {
    vpc_id = aws_vpc.main_vpc.id
    cidr_block = "10.123.1.0/24"
    map_public_ip_on_launch = true
    availability_zone = "us-east-1a"
    tags = {
        Name = "dev-public"
    }
}

--> terraform plan
--> terraform apply
```
* create api gateway
```
resource "aws_internet_gateway" "main_internet_gateway" {
  vpc_id = aws_vpc.main_vpc.id
  tags = {
    Name = "dev-igw"
  }
}
```
* create route table
```
resource "aws_route_table" "main_public_route_table" {
  vpc_id = aws_vpc.main_vpc.id

  tags = {
    Name = "dev-public-rt"
  }
}
```
* create route on route table that sets the output as public internet through the internet gateway
```
resource "aws_route" "default_route" {
  route_table_id         = aws_route_table.main_public_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.main_internet_gateway.id
}
```
* associate the subnet with the route table
```
resource "aws_route_table_association" "main_subnet_route_table_assoc" {
    subnet_id = aws_subnet.main_public_subnet.id
    route_table_id = aws_route_table.main_public_route_table.id
}
```
* add a security group that defines how data can flow into and out of the vpc 
```
resource "aws_security_group" "allow_tls" {
  name        = "dev-sg"
  description = "dev security group"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    protocol    = "-1"
    to_port     = 0
  }

  egress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    protocol    = "-1"
    to_port     = 0
  }
}
```
* add data source for an EC2 instance of ubuntu (note the use of "data" vs "resource" because amis are not infrastructure)
```
// tells terraform to use the aws ami list to get the specified information and then store the result in a variable named "main_server_ami"
//  filter command filters the available amis according to query specified

data "aws_ami" "main_server_ami" {
    most_recent = true
    owners = ["099720109477"]

    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]
    }
}
```
* add a keypair to use for the eventual ec2 instance:
    * generate an ssh key from the shell: 
    ```
     ssh-keygen -t ed25519
    ```
    * add generated keypair file as resource to terraform deployment
    ```
    resource "aws_key_pair" "mtc_auth" {
        key_name = "mainkey"
        public_key = file("~/.ssh/mainkey.pub")
    }
    ``` 
* add ec2 instance & install docker on it
    * crate user data template file with has shell script to run on ec2 instance
    ```
    #!/bin/bash
    sudo apt-get update -y &&
    sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common &&
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - &&
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" &&
    sudo apt-get update -y &&
    sudo sudo apt-get install docker-ce docker-ce-cli containerd.io -y &&
    sudo usermod -aG docker ubuntu
    ```
    * create resource: (set user_data method to point to userdata.tpl file so that it knows what to run)
    ```
    resource "aws_instance" "main-node" {
        instance_type          = "t2.micro"
        ami                    = data.aws_ami.main_server_ami.id
        key_name               = aws_key_pair.mtc_auth.key_name
        vpc_security_group_ids = [aws_security_group.allow_tls.id]
        subnet_id              = aws_subnet.main_public_subnet.id
        user_data              = file("userdata.tpl")

        root_block_device {
            volume_size = 10
        }

        tags = {
            Name = "main-node"
        }
    }
    ```
    * verify instance by getting public ip of ec2 instance
    ```
    // from command line
    terraform state show aws_instance.main-node
    // get public_ip from the result of the above state request
    // ssh into box from command line
    ssh -i ~/ssh/mainkey ubuntu@<publicip from above>
    // verify docker installation
    docker --version
    ```