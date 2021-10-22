# Architecting on AWS 

## Questions
* How do you group resources that are used for a paricular solution you are building? (Answer: Use Resource Groups)[https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html]
* How do you see ALL resources that you are using in your AWS account (across regions/azs/etc)? (Answer: Use Resource Groups and Tag Editor)[https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/]
* Is it easy to transfer a resource between Regions/AZs and is there a cost for that? (Answer: For S3 buckets, you cant move the s3 bucket itself so you move the contents of the s3 bucket.  One way to do that for S3 buckets is to use cross-region replication)[https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html]

## Labs
**Hosting a static website**
- create an s3 bucket
- make it publicly available
- select it -> go to properties -> enable static website hosting
- upload files
- mark all uploaded files that need to be accessed externall as public (select file(s) -> click on "actions" button -> Select "Make Public")
- **Note** - each time you upload a new file (even if its replacing an existing one), it goes back to being not available publicly

**Deploying a web application**
* deploy security at every layer of application
    * Create a VPC
    * Create security group for app (public subnet)
        * Look up EC2
        * Select Security Groups in left menu
        * Create Security Group
            * Tie Security group to VPC
            * Create Inbound rules that allow for HTTP calls
    * Create security group for db (private subnet)
        * Look up EC2
            * Select Security Groups in left menu
            * Create Security Group
                * Tie Security group to VPC
                * Create Inbound rules that allow for MYSQL/Aurora, Custom, click magnifying glass and select Security Group Name that you made for the applicatio
    * Create RDS Database instance
        * Go to RDS -> Create Database -> Add DB instance to DB Security Group
    * Launch EC2 Instance for application server
        * Go to EC2
            * Launch Instance
            * select AMI and click Configure buton
            * Network => Set to VPC created initially
            * Subnet => **Are these subnets the ones that are available or were they created previously for this lab**
            * Select IAM Role
            ```
            // this role grants permission to access the inventory-app settings wihtin the AWS Systems Manager Parameter Store which will be used to store configuration settings 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "ssm:*",
            "Resource": "arn:aws:ssm:*:*:parameter/inventory-app/*",
            "Effect": "Allow"
        }
    ]
}
            ```
            * Configure EC2 instance to run script when the instance starts up via the Advanced Details => User Data field
                * Script installs Apache web server (httpd), downloads the inventory application and the AWS SDK, activate the web server and configure it to auto boot on start
            ```
#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd mysql
amazon-linux-extras install -y php7.2
# Download Lab files
wget https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-200-ARCHIT/v6.8.18/lab-2-webapp/scripts/inventory-app.zip
unzip inventory-app.zip -d /var/www/html/
# Download and install the AWS SDK for PHP
wget https://github.com/aws/aws-sdk-php/releases/download/3.62.3/aws.zip
unzip aws -d /var/www/html
# Turn on web server
chkconfig httpd on
service httpd start
            ```
            * Add Storage (default is usually fine unless theres a specific need for another one)
            * Add Tags
            * Configure Secuirty Group
                * Select App Security Group 
            * Start Instance (Generate key pair so that you can access it programmatically)
            * Click on view instances => Status for this EC2 is probably pending.  wil be available when "running" is status




**Creating a VPC**
* Create a VPC
    * CIDR Range 16 (10.0.0.0/16 => includes all IP addresses that start with 10.0.x.x.  This range contains 65,000 IPs)
* Go back to VPC listing, select VPC that was created and select Actions => Edit DNS hostnames => Enable DNS hostnames (indicates whether instances with public IP addresses get corresponding public DNS hostnames)
    * Selecting this any amazon EC2 instance launched into this VCP will now automatically receive a DNS hostname.  You can make a more meaningful DNS name using Amazon Route 53
* Create a subnet - From VPC service page -> select "Subnets"
    * Create a public subnet 
        * Click Create Subnet -> Select VPC to attach this subnet to -> give it a name -> Choose an AZ -> Choose 10.0.0.0/24 for CIDR block (includes all IP addresses that start with 10.0.0.x IP addresses.  This is SMALLER than the allowed IPs that were defined for the VPC)
        * Go back to Subnet listings -> select public subnet created -> click on actions -> Modify auto-assign IP settings -> enable auto-assign public ipv4 address
        * At this point subnet is still not public because you a public subnet needs to be tied to an internet gateway to have access outside the VPC
    * create a private subnet
        * Click Create Subnet -> Select VPC to attach this subnet to -> give it a name -> Choose an AZ -> Choose 10.0.2.0/23 for CIDR block (includes all IP addresses that start with 10.0.2.x and 10.0.3.x IP addresses.  This is SMALLER than the allowed IPs that were defined for the VPC)
* Create an internet gateway - horizontally scaled, redundant, and HA VPC component that allows communication between instances in a VPC and the internet. 
    * Serves two purposes
        * provide a target for route tables to connect to the internet
        * perform network address translation (NAT) for instances that have been assigned public IPv4 addresses
    * Create IGW
* Attach IGW to Public Subnet
    * Go to VPC/IGW page => Select IGW that was created => click on Actions => Select Attach to VPC => Select VPC that contains the public subnet
* Configure Route Table - A route table contains a set of rules, called routes, which are used to determine where network traffic is directed.  Each subnet in a VPC must be associated with a route table; the table controls teh routing for the subnet.  A subnet can only be associated with one route table at a time but you can associate multiple subnets with the same route table.  
    * To use an internet gateway, a subnet's route table must contain a route that directs internet-bound traffic to the internet gateway.  If a subnet is associated with a route table that has a route to an internet gateway it is known as a public subnet.
    * From VPC page -> Hover over name of route table that is tied to the VPC created and rename it "Private Route Table"
    * Create a Public Route Table -> Select "Create route table" -> Name it Public Route Table -> Tie it to the same VPC
        * Go to Route Table listing and select Public Route Table => Click on "Routes" in the tabs on the bottom => Clkick Edit Route Table
        * Click Add Route => Destination: 0.0.0.0/0, Target: Internet Gateway (select IGW created above)  => Save Changes
    * Associate Public Route Table with Public Subnet
        * Select Public Route Table => Subnet Associations Tab => Edit subnet associations => Select Public Subnet => Save Changes
        * Now Public Subnet has public access
* Create Security Group for the App Server - Security Group acts as a virtual firewall for instances to control inbound and outbound traffic.  Security Groups operate at the instance network interface level not the subnet level.  Therefore, each instance can have its own firewall that controls traffic.  If you do not specify a particular security group at launch time , the instance is automatically assigned to the default security group for the VPC.
    * From VPC page => Select Security Groups => Create Security Group
        * Add name, description, attach to VPC
        * Add invound rule => type: http, Source: anywhere => Save (This creates a security group that allows traffic over port 80 and coming from anywhere on the internet)
* Launch an EC2 instance into the public subnet and confirm the app server is accessible from the internet
    * Got to EC2 => Launch Instance => Select Amazon Linux 2 AMI t3 micro => Lab VPC, Public Subnet, IAM: Inventory-AppRole => Add Advance Details/User Data
    ```
#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd mysql
amazon-linux-extras install -y php7.2
# Download Lab files
wget https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-200-ARCHIT/v6.8.18/lab-2-webapp/scripts/inventory-app.zip
unzip inventory-app.zip -d /var/www/html/
# Download and install the AWS SDK for PHP
wget https://github.com/aws/aws-sdk-php/releases/download/3.62.3/aws.zip
unzip aws -d /var/www/html
# Turn on web server
chkconfig httpd on
service httpd start
    ```
    * Configure Security Group => Select Existing => App-SG
    * Launch Instance
    * Once Running => Select EC2 intance => IN details tab, copy public ipv4 address => http://<ipv4 address>
* Configure VPC Peering - A networking connection between two VPCs that enables you to route traffic between them privately.  Instances in either VPC can communicate with each other as if they are within the same network.  You can create a VPC peering connection between your own VPCs, with a VPC in another AWS account or with a VPC in a different AWS Region.
    * VPC => Peering Connections => Create Peering Connection => Name it and Select Request/Acceptor
        * When a peering connection is created the target VPC MUST accept it.  This is because the target VPC might be owned by a different account or the user creating the peering conn might not have permission to accept the connection for the target VPC.  
        * Go to Peering COnnections page, select the Peering connection created, click on actions, Accept Peering connectio
* Configure Route Tables to send traffic from the Lab VPC to the peering connection
    * Configure Lab VPC => Shared VPC Connection    
        *  Select route tables => select lab public route table => from tabs below, select routes and click on Edit routes => add route destination 10.5.0.0/16 (this si the CIDR range of the shared vpc) with target = peering connection -> select the peering connection => Save changes
    * Configure Shared VPC => Lab VPC connection
        *  Select route tables => select shared public route table => from tabs below, select routes and click on Edit routes => add route destination 10.0.0.0/16 (this si the CIDR range of the lab vpc) with target = peering connection -> select the peering connection => Save changes

**Creating a HA (highly available) Environment**
* Create an ALB - balances traffic between multipel App Servers.
    * Go to EC2 -> Select Load Balancers -> Create Load Balancer
    * Select the VPC that the subnets are in.  
    * Select which AZs the ALB will communicate with and then select which subnets within those AZs the App Servers will reside.
    * Attach a security group for the ALB that allows for incoming/outgoing http traffic
        * Click on create security group.  
        * Add an Inbound Rule: Http from anywhere 
        * Add an Inbound Rule: Https from anywhere
    * Attach ALB Routing - **Target Groups** define where to SEND traffic that comes into the balancer.  The ALB can send traffic to multiple target groups based on the URL of the incoming request.  For example, requests from mobile apps could be sent to different set of servers.  
        * In Listners & Routing -> Click Create Target Group
        * You want ALB to go directly to EC2 instances so select Instances
        * Select the VPC
        * Click Next
        * Select the Servers that are included in this target group
    * Make App Layer HA - Generate Auto Scaling Group
        * Generate Launch Template - This will be used by the Scaling Group to generate a new EC2 when necessary
            * Go to EC2 -> Launch Templates -> Create Launch Template
            * Select an AMI, Instance Type, Security Group (should be same same security group that was attached to the ALB), Set an IAM profile, Add the User data script, create template
        * **Best Practice** - Auto Scaling Groups should be built across private subnets.  Use Load balancers for public and ASGs for private.
        * Create ASG
            * Go to EC2 -> Auto Scaling Groups -> Create Auto Scaling Group -> Select Launch Template generated above
            * In Network Settings -> Select VPC that EC2s will reside in -> Select the private subnets that the ASG will work across
            * (optional) Attach to an existing load balancer -> Select ALB created above -> Tell ASG to create new EC2 instances in the Target Group created above
            * Configure group size and scaling policy => Set desired, min, max capacities
                * if the app is expected to receive varying loads of traffic, then you should crate a **scaling policy** that defines when to launch/terminate instances 
            * Add Tags to the ASG, that way when new EC2 instances are created, they will have the tag that you specify here and you'll know it was generated by ASG
    * Create Security Groups per Layer (i.e. web, app, db)
        * web SG was craeted when we created ALB
        * Create app SG that will be applied to each App server that is generated in ASG
            * Go to Security groups and select or create Security Group that will be applied t App servers
            * Go to inbound rules and add a rule allowing traffic to come in from ALB -> HTTP, in box to the right of Source select ALB
        * Create db SG that will be applied to the db
            * Go to Security groups and select or create Security Group that will be applied t App servers
            * Go to inbound rules and add a rule allowing MYSQL/Aurora traffic to come from App Servers -> Type: MYSQL/Aurora, in box to the right of Source, select Security Group tied to App servers
    * Testing HA
        * Go to EC2 -> Instances -> Select one of the EC2 instances tied to the ALB and terminate it.  Verify that the site can still be hit
    * Make DB Layer HA - 
        * Go to Amazon RDS -> Select instance that you want to make HA
        * Go to Availability & Durability and select "Create a standby instance"
            * This will create a new db in another AZ that will be COLD and used in failover only.
    * Make Outgoing Comms from App Servers HA
        * Incoming connections are now HA because of load balancer and ASG.  But App Servers should be able to send information out. Sending information out goes through NAT Gateways.  Want to create a NAT Gateway for each AZ.
        * Go to VPC -> NAT Gateways -> Create NAT Gateway -> Select Subnet that resides in the second AZ -> Allocate Elastic IP -> Create NAT Gateway
        * Create Route Table for Private Subnet 2 that redirects traffic to the new NAT gateway => EC2 => Route Tables => Create => Select VPC => Create
        * Update the route table so that any internet bound traffic goes through this NAT gateway => Select Route Table that was created => Click on Routes Tab => Edit Routes => Destination: 0.0.0.0/0 (internet), Target: NAT Gateway/NAT gateway created above
        * Attach the NAT Gateway to the appropriate subnet => EC2 => Route Tables => Select Route Table => Subnet Associations Tab => Select both private subnets => save changes




**Automating infrastructure deployment with AWS Cloud Formation**
* **Best Practice** - deploy infrastructure in layers
    * Common Layers Networking, Application, DB
* Go to Cloud Formation -> Create Stack -> With new resources -> upload file
* Events show whats happening
* Resources show all resources that are being worked on 
* Outputs show the ids of specific resources and links to resources
* A Cloud Formation stack can reference other stacks
```
  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable HTTP ingress
      VpcId:
        Fn::ImportValue:
          !Sub ${NetworkStackName}-VPCID

```

**Implementing a Serverless Architechture with AWS Managed Services**
* Create Lambda to process inventory file
    * Lambda -> Create Function -> Author from scratch -> Python -> Use Existing Role (role was created prior to lab). Role Contains: 
 ```
    AmazonDynamoDBFullAccess
    AmazonS3ReadOnlyAccess
    CWLogsPolicy
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*",
            "Effect": "Allow"
        }
    ]
}
```
    * Copy this code into the Lambda Function and Deploy
```
    # Load-Inventory Lambda function
#
# This function is triggered by an object being created in an Amazon S3 bucket.
# The file is downloaded and each line is inserted into a DynamoDB table.

import json, urllib, boto3, csv

# Connect to S3 and DynamoDB
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

# Connect to the DynamoDB tables
inventoryTable = dynamodb.Table('Inventory');

# This handler is run every time the Lambda function is triggered
def lambda_handler(event, context):

  # Show the incoming event in the debug log
  print("Event received by Lambda function: " + json.dumps(event, indent=2))

  # Get the bucket and object key from the event
  bucket = event['Records'][0]['s3']['bucket']['name']
  key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
  localFilename = '/tmp/inventory.txt'

  # Download the file from S3 to the local filesystem
  try:
    s3.meta.client.download_file(bucket, key, localFilename)
  except Exception as e:
    print(e)
    print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
    raise e

  # Read the Inventory CSV file
  with open(localFilename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    # Read each row in the file
    rowCount = 0
    for row in reader:
      rowCount += 1

      # Show the row in the debug log
      print(row['store'], row['item'], row['count'])

      try:
        # Insert Store, Item, and Count into the Inventory table
        inventoryTable.put_item(
          Item={
            'Store':  row['store'],
            'Item':   row['item'],
            'Count':  int(row['count'])})

      except Exception as e:
         print(e)
         print("Unable to insert data into DynamoDB table".format(e))

    # Finished!
    return "%d counts inserted" % rowCount
```
    
* Configure Amazon S3 Event 
    * S3 -> Create bucket
    * Click on Bucket -> Properties Tab -> Event Notifications -> Create Event Notification -> Select "All Object Create Events" -> Specify Lambda to trigger
* Configure Notifications
    * SNS -> Create Topic Name -> Standard
* Create Subscription to Notifications
    * Select the topic you want to subscribe to -> click Subscriptions Tab -> Create Subscription
* Create Lambda triggered on record insert to dynamo db to publish messge on SNS
    * Lambda -> Create Function -> Author from scratch -> Python -> Use Existing Role (role was created prior to lab). Role Contains: 
```
AWSLambdaDynamoDBExecutionRole
AmazonSNSFullAccess
```
    * Copy this code into the Lambda Function and deploy: 
```
# Stock Check Lambda function
#
# This function is triggered when values are inserted into the Inventory DynamoDB table.
# Inventory counts are checked, and if an item is out of stock, a notification is sent to an SNS topic.

import json, boto3

# This handler is run every time the Lambda function is triggered
def lambda_handler(event, context):

  # Show the incoming event in the debug log
  print("Event received by Lambda function: " + json.dumps(event, indent=2))

  # For each inventory item added, check if the count is zero
  for record in event['Records']:
    newImage = record['dynamodb'].get('NewImage', None)
    if newImage:

      count = int(record['dynamodb']['NewImage']['Count']['N'])

      if count == 0:
        store = record['dynamodb']['NewImage']['Store']['S']
        item  = record['dynamodb']['NewImage']['Item']['S']

        # Construct message to be sent
        message = store + ' is out of stock of ' + item
        print(message)

        # Connect to SNS
        sns = boto3.client('sns')
        alertTopic = 'NoStock'
        snsTopicArn = [t['TopicArn'] for t in sns.list_topics()['Topics']
                        if t['TopicArn'].lower().endswith(':' + alertTopic.lower())][0]

        # Send message to SNS
        sns.publish(
          TopicArn=snsTopicArn,
          Message=message,
          Subject='Inventory Alert!',
          MessageStructure='raw'
        )

  # Finished!
  return 'Successfully processed {} records.'.format(len(event['Records']))
```
    * Click "Add Trigger" -> Select Dynamo DB -> Select Table 
