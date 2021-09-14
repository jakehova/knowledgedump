# Rough Notes

## Weakpoints
* Networking
* IAM

## Questions 
* Is there a charge for using RDS vs standing an EC2 with MySQL up?
* **WTF** What the fuck is CIDR.  need to see how many IPs are available based on multiple CIDR values
* **WTF** What is a NAT gateway?
* What is Layer 7 or 4 with regards to the ELB?
* Step Scaling is a best practice.  Need to look that up 

## Networking Part 2
**Virtual Private Gateway (VGW)** - Connecting OnPrem to AWS
    * Enables you to establish private connections (VPNs) between an Amazon VPC and another network
    * Provides two endpoints 
    * **VPN Cloud Hub** Can provide multiple VPN connections to multiple networks connected to one VGW
**AWS Direct Connect** - provides you with dedicated private network connection of either 1 or 10Gbps
    * Hybrid Cloud Architechtures
    * Contrinually transferring large data sets
    * Network Performance predictability
    * Security and Compliance
    * CONS: May require need to setup physical network circuits to setup a direct connect
    **Note:** - Good to setup a backup VPN connection through a different internet service provider as a backup to Direct Connect in case Direct Connect goes down
**VPC Endpoint** - privately connect your EC2 instances to services outside your VPC (without leaving AWS)
    * Dont need to use internet gateway, VPN, network address translation (NAT) devices
    * Types
        * Interface Endpoint
        * Gateway Endpoint 
            * Amazon Simple Storage Service (S3)
            * Dynamo DB
**Elastic Load Balancing (ELB)** - managed load balancing service that distributes incoming application traffic across multiple EC2s or services
    * uses http, https, tcp, ssl 
    * external/interal facing
    * each load balancer is given a DNS name
    * performs health checks and resolves most 
    * Types
        * Application Load balancer
            * flexible app mgmt
            * advanced load balancing of http/https traffic
            * Operates at request level (Layer 7)
        * Network Load balancer
            * Extremem performance and static IP for your application
            * Load balancing of TCP, TLS, UDP traffic
            * Operates at the connection level (Layer 4) 
        * Classic Load Balancer - deprecated
    * Deregistration delay - remove an instance from elb options without affecting users (delays registration until that that node is complete with its processing)
**High Availability**
    * Design for no single point of failure and duplicative environment in at least 2 AZs (i.e. two app servers pointing to one db is BAD.)
    * RDS generates does auto fail over 
**Route 53** - highly available and scalable cloud Domain Name System (DNS) service (port 53 is used for DNS which is where Route 53 is named the way it is)
    * Performs regular DNS Health Checks (can perform automatic fail overs)
    * Routing options
        * Simple Round Robin - just go one elb at a time
        * Weighted Round Robin - go to preferred elb 
        * Latency-based routing - route based on latency of networks
        * Health Check and DNS failover - active/passive failover
        * Geolocation routing - route based on user location
        * Geoproximity routing with traffic biasing - route based on user location and 
        * Multi-value answers - 


## IAM -
* Root User has unlimited access to your AWS account.  Cannot be limited. NEVER USE ROOT USER
* Identity Based Policy
    * Attached to: User, group, or role
* IAM Groups
* IAM Roles - A role lets you define a set of permissions to access the resources that a user or service needs
    * Use Cases: 
        * AWS Resources with access to AWS services
        * Provide access to externally authenticated users
        * Provide access to third parties 
        * Can be used to grant credentials temporarily 
* Using Groups vs Using Roles
    * Roles are for individual things (users or services).  Groups are for users.  Your employees/contractors would be part of groups.  If one of them needs access to a service or environment temporarily, then you would create a role and assign that role to them. 
* STS Identity Broker
* SAML 
* **AWS Cognito** - fully managed service that provides authentication, authorization, and user management for web/mobile apps
    * User Pools - user directory 
    * Identity Pools - federated identities - create uniqe identies for your users and federate them with your users
* **AWS Landing Zone** - helps customers more quickly set up a secuire, multi-account AWS environment based on AWS best practices
* **AWS Organizations** - Centralized account management
    * NO CHARGE & BEST PRACTICE To manage users 
    * Group-based account management
    * Policy-based access to AWS Services
    * Automated account creation and management
    * Consolidated billing
    * API-based
    * Root has OUs. OU has AWS Account * Resources. Service Control Policies apply to each layer.

## Elascity/HA
**Scalability**
* Types 
    * Time BAsed - turn off resources when they are not being used
    * Volume based - match scale to the intensity of your demand 
    * Predictive Based - predict future traffic based on daily/weekly trends
* Monitoring
    * **AWS Cost Explorer** - Monitor your service usage and respective cost along with generating estimations for future use.
    * **Amazon CloudWatch** -
        * collects and tracks metrics for your redsources
        * enables you to create alarms and send notifications
        * can trigger changes in capacity in a resource based on rules you set 
        * Targets: Metrics, Logs, Alarams, Events, Rules, Targets(Services like SNS, SQS, etc)
    * **AWS CloudTrail** - Records all API calls made in your account and saves logs in your designated S3 bucket
    * **VPC Flow Logs** - Catpures traffic flow details in your VPC
        * Can be enabled at VPC, subnet, or ENI level
    * Things you want to monitor
        * Operational Health
        * Resource utilization
        * App Performance
        * Security Auditing 
* **Amazon EC2 Auto Scaling**
    * Types
        * Scheduled - good for predictable workloads (i.e. turning off dev and test instances at night)
        * Dynamic - excellent for general scaling (scaling based on CPU utilization)
        * Predictive
    * How - Adds EC2 to Auto Scaling Group.  When adding to auto scaling group, can pick on-demand or spot scaling for that group
    * **Auto Scaling Group (ASG)** - Set Desired, min, max capactiy with regards to # of EC2 instances.  
        * Question: Whats a good min/max capactiy to set => use trial and error 
    * Considerations 
        * Might need to combine multiple types of autoscaling
        * architechture might require  more hands scaling using **Step Scaling**
        * some architechtures need to scale on two or more metrics (not just CPU)
        * scale out early and fast, while scaling in slowly over time.  Scale out means expand.  Scale In means condense.
        * use lifecycle hooks 
            * perform custom actions as auto scaling launches or terminates instances 
    * Scaling your Database     
        * Read Replicas
            * horizontally scaling read-heavy workloads
            * offload reporting
            * Aurora can have up to 15 read replicas spread across multiple AZs
            * Considerations
                * replication is async so potential for reading stale data.
                * avail for Aurora, MySQL, MariaDB, PostgreSQL, Oracle
        * Push Button Scaling 
            * Vertical scaling up/down.
        * Scaling Amazon RDS write with Database Sharding (sharding is partitioning the data where each partition is in its own database)
        * Aurora Serverless - responds automatically to usage.  scales capacity, shuts down, starts up on its own.
            * pay for the number of ACUs used
            * good for spiky, unpredicatable workloads