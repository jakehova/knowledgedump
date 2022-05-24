# Terraform

## How is it processed
* All "tf" files are treated as if they are in the same file. as long as it's in the same directory.  Terraform will parse out the files and create a plan and order of operations for applying all the configuration objects in the tf files in the same directory that the terraform command is run in.

## Setup
### Setup AWS User
1) Create User to impersonate for Terraform tasks and where it comes from
2) assign AdministratorAccess permissions 
3) Update .aws credentials file with Programmatic access creds

### Setup VS Code
1) Install AWS Toolkit extension
2) Select .aws credentials profile that was created in other step
3) Install HashiCorp Terraform extension

### Setup Provider - providers.tf
A provider is a platform that you are targeting (docker, aws, gcp, etc). you define the platform and what library is managing it in the "required_providers" node.  Then you provide the details of the provider in the "provider "<platform>"" node (~ references the home directory). 
```
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

### Setup Initial terraform entry
* Run: terraform init
  * this creates:    
    * terraform.lock.hcl file - this operates to make sure provider library is same version consistently (package.json parallel)
    * .terraform folder    
    * in .terraform folder you will have compiled result 
* important files: 
  * **terraform.lock.hcl**
    * stores the provider attributes so terraform knows what versions of things to use for providers
    * similar to package.json.lock
* file types
  * tf: terraform file
  * tpl: template file 
  * tfvars: takes variables defined in variables.tf file and provides values for them.  This file cannot declare new variables
  * variables.tf: define variables and, optionally, their default values
  * main.tf: defines the terraform block
  * providers.tf: defines the providers 
  * versions.tf: defines the required versions for items being run

## Common Commands
* initialize state: **terraform init**
* show state: **terraform show**
* show plan: **terraform plan <-destroy>**
* apply plan: **terraform apply <-auto-approve>**
* format terraform files: **terraform fmt**
* get into terraform console: **terraform console**
* destroy entirety of terraform generated resources: **terraform destroy**

## Debugging
* Set TF_LOG environment variable to "DEBUG"
  * Powershell: **$env:TF_LOG="DEBUG"**
* Confirm the aws role that is running the commands: **aws sts get-caller-identity**


## Resources
* Resources are defined as infrastructure objects OR data elements that are defined outside of 
* data - this type of resource requests that Terraform read from a given data source and then export that result as the name provided

### Configure Resources
* [AWS Resources List](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
* format of resource definition: 
```
resource "<resource name>" "<terraform logical identifier  that you will reference this resource by in your terraform scripts>" {
  <properties of resource>
}

i.e.

resource "aws_default_vpc" "default-vpc" {
  tags = {
    Name = "Default VPC"
  }
}
```
* format of data definition: 
```
data "aws_ami" "main_server_ami" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]
  }
}
```

### Referencing Resources
* When needing to reference the properties of another created resource, use the resource identifer and name and property to pull the value
  * i.e. vpc_id = aws_default_vpc.default_vpc.id

## [Variables](https://www.terraform.io/language/values/variables)
* Declare variables via (in order of precedence (least to most)): 
  * env variables
  * terraform.tfvars file (default variable file name)
  * *.auto.tfvars files
  * -var="<variablename>=<variablevalue>" or -var-file="<variable file name to use>" from the command line as an argument 
* native variable types are: 

* initialize variables by: 
```
variable "<variables name>" {
  type = string || number || bool
}

variable "<other variable name>" {
  type = list(string)
  default = ["us-west-1a"]
}

variable "<another variable name>" {
  type = list(object({
    internal = number
    external = number
    protocol = string
  }))
  default = [
    {
      internal = 8300
      external = 8300
      protocol = "tcp"
    }
  ]
}
```
* To reference a variable in terraform code, prefix with var: ${var.<variable name>}


## State
* to see entire current state, run: **terraform show**
* to see all resources in state, run: **terraform state list**
* to see state of particular resource, run: **terraform state show <resource id>.<resource name>** (i.e. - terraform state show aws_vpc.main_vpc)
* Stored in terraform.tfstate file
  * can be stored locally, in the cloud, in aws, etc 

## [Provisioner](https://www.terraform.io/language/resources/provisioners/syntax)
* model specific actions on the local/remote machine to preapre servers or other infra objects for service
* **IMPORTANT** - This is a tool of LAST RESORT.  You only need this if there's no way to do what you need via terraform scripts directly
* Terraform does NOT detect provisioner code as a change to state, so to get it to trigger a deploy use "terraform apply -replace <resource name>" to force a re-run of the resource

```
 provisioner "local-exec" { // CANNOT have "_" in name, need to use hyphens
    command = templatefile("windows-ssh-config.tpl" // template file used, 
    {  // variables substitution for file 
      hostname = self.public_ip,
      user = "ubuntu",
      identityfile = "~/.ssh/mainkey"
    })
    interpreter = var.host_os ? "windows" ? [  "Powershell",  "-Command" ] : ["bash","-c"] // what interpretor to use on the machine
  }
```

## Variables
* **variables.tf** is used to define variable TYPES and, optionally, set default values
* **<filename>.tfvars** is used to SET the values of those variables and is passed as a command line argument to the apply method
  * this file cannot create new variables


## [Output](https://www.terraform.io/language/values/outputs)
* Allows you to output values that are associated with the resources that were deployed from the console
* Defined outputs are shown in the tfstate file
```
output "dev_ip" {
  value = aws_isntance.main_node.public_ip
}
```

## Notes
* Handling Mismatching
  * discrepancy between lock file and current terraform configuration
    * terraform init -upgrade
  
  
* Create a KeyPair: 
```
// from the terminal: 
ssh-keygen -t ed25519
// save key to .ssh folder (copy folder that is suggested and just give a better key name)
// verify that file is in ssh folder
ls ~/.ssh+

```
* add ssh config
  * use windows-ssh-config.tpl
  ```
  add-content -path ~/.ssh/config -value @'

  Host ${hostname}
    HostName ${hostname}
    User ${user}
    IdentityFile ${identityfile}
  '@
  ```
