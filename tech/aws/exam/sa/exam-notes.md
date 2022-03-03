# Exam Notes

## Questions to ask for anyquestion in the exam
* Can it be cached
* What kind of cache should be used? (i.e if its a DB, then Redis/Memcache/DAX if its a web request then Cloud Front, IP caching mea)
* How does the content get updated? (TTL usually)
* Does it add anything besides speed? (with cloudfront it adds security and high availablity and speed)

# Solution Architect Exam Notes
- A region is a physical location in the world that consists of 2 or more AZs
- An AZ is one more discrete data center house in separte facilities each with redundant power, netowrking, and connectivity
- AN Edge Lcoation endpoints for AWS used for caching content.  Usually consists of CloudFront.
- (Well Architected Framework)[https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html?did=wp_card&trk=wp_card]
- Shared Responsibility Model - You are responsible for Security IN the cloud (customer data, authorization/authentication, encryption, etc) and AWS is responsible for Security OF the cloud (hardware, software)
- Key Services to Know: 
    - Compute: EC2, Lambda, Elastic Beanstalk
    - Networking: VPC, Direct Connect, Route 53, API Gateway, AWS Global Accelerator
    - Storage: S3, EBS (Elastic Block Store), EFS (Elastic File Service), FSx, Storage Gateway
    - Databases: RDS, DynamoDB, Redshift 
- Securing Root Account: 
    - Enable MFA
    - Create an Admin Group for your admins and assign the appropriate permissions to that group
    - Create user accounts for admins
    - Add users to the admin group
- You control access to AWS via IAM which uses Policy Documents (JSON)
- IAM is global; it does not apply to regions.
- The root account should be locked down immediately and never used for day to day activities.  Should then create an admin group and add user accounts to that. 
- Access Key ID and secret Access Keys are not the same as username and passwords; they are for programmatic console access.  They cannot be used to log in to the console.
- IAM Federation is used to combine your existing user account mgmt platform (usually Active Directory) with AWS via SAML standard (SAML Standard is Active Directory)

Key Words: 
File Storage means likely not S3.  Maybe EFS or FSx

**OSI Model**
* conceptual framework used to describe functions of a networking system.
* 7 layers: 
    1 Physical layer - transmission and reception of raw bit streams over a physical medium ( network hubs, cabling, repeaters, network adapters, modems, etc)
    2 Data link layer - reliable transmission of data frames between two nodes connected by a physical layer
    3 Network layer - Addressing, routing, traffic control
    4 Transport layer - reliable transmission of data segments between poinst on a network (segementation, acknowledgement, multiplexting)
    5 Session layer - continuous exchange of info in the form of multiple back-and-forth transmissions between two nodes
    6 Presentation layer - Character encoding, data compression, encryption/decryption
    7 Application Layer  - High Level APIs

**VPC communication**
* AWS Transit Gateway connects your VPC to on-prem networks through a central hub
* AWS Direct Connect establishes a dedicated network connection from on-prem to AWS
* AWS VPN CloudHub is used to provide secure communication between remote sites 
* VPC endpoint without leaving AWS (private connection) then use VPC Endpoint

**EC2**
* During Scale-In, default termination policy is to remove the instance with the oldest configuration. 
* Nitro EC2 instances are the newest versions and can do 64k for a provisioned IOPS SSD.  Other versions can only do up to 32k
* Storage Comparison:
    * SSD - Small & Random I/O ops, can be bootable, best for transactional workloads, critical apps that require sustained IOPS, large db workloads.  
        * General Purpose - boot volumes, virtual desktops, most workloads
        * Provisioned IOPS - for more than 16000 IOPS or 250 MiB/s, and large datasets (databses)
    * HDD - Large & Sequestion I/O ops, NOT bootable, best for large streaming workloads, big data/data warehouses/log processing, 
    * EBS - block-level storage device that is durable
        * Use for data that requires frequent updates (system drive for an instance or databse app or througput intensive apps)
        * They persist independently of the life of an EC2 instance
        * Automatically replicated within an AZ
        * Support live config changes (can modify volume type, volume size, and IOPS capacity w/o service changes)
        * Uses 256 bit AES encryption
        * Snapshots are sent to S3
        * **NOTE** does NOT support object/file lock
* Scaling   
    * Simple Scaling - waits for a cooldown period (default to 300 seconds) to expire before spinning up the next instance
        * Target Tracking Scaling - increases or decreases instances based on the target value of a metric.  Scales out or in to keep as close to target value of metric as possible
        * Scheduled Scaling - scales based on predicted patterns
        * Suspend/Resme Scaling - temporarily pauses scaling activities
* Metadata
    * Instance metadata - data about your instance that you can use to configure/manage running the instance 
        * Instance ID
        * Public IP
        * Public Keys
    * User Data - used to perform common automated config tasks and run scripts after the instance starts
* Placement Group
    * used to provide low-latency network perf for tightly copuled node-to-node communication

**Amazon Lightsail**
* offers cloud servers for really cheap prices

**Amazon Data Lifecycle Manager (DLM)**
* automate creation, retention, deletion of snapshots taken to backup your EBS volumes. 

**Application Load Balancer (ALB)**
* routes traffic to targets (EC2, containers, IP addresses, Lambdas) based on the content of the request
* ideal for load balancing http/https traffic.
* Routing Strategies
    * host-based: based on the host field of the http header
    * path-based: based on the URL of the http header
    * http header-based: based on value of any standard or custom HTTP header
    * http method-based: based on any standard or custom HTTP method
    * query string parameter-based: based on query string or query parameters
    * source ip address CIDR-based: based on source IP address CIDR from where the request originates
* DOES support SNI

**Network Load Balancer (NLB)**
* routes traffic to targets
* does NOT support path-based routing or host-based routing

**Classic Load Balancer (CLB)**
* use for aps that are built within the EC2-Classic network only.
* does NOT support path-based routing or host-based routing
* does NOT support SNI

**Gateway Load Balancer (GLB)**
* used for deploying, scaling, and running 3rd party virtual appliances.  
* does NOT support path-based routing or host-based routing

**CloudFront**
* Used as a CDN - delivers content from each edge location
* Uses Server Name Indication (SNI) to provide https. 
    * SNI is an extension of TLS
    * Setup: 
        * CloudFront associates your alternate domain name with an IP address for EACH edge location
        * When a viewer submits an https request for content, DNS routes the request to the IP address for the proper edge location
            * The IP address to your domain name is determined during the SSL/TLS handshake.
    * Request Process: 
        * viewer makes https request for content
        * viewer automatically gets the domain name from the request url and adds it to the request header
        * CloudFront receives the request, finds the domain name in the request header, and responds to the request with the applicable SSL/TLS cert
        * viewer and CloudFront perform SSL/TLS negotiation
        * CloudFront returns the requested content to the viewer
    * If you have to support browsers that do not support SNI, then use dedicated IP addresses in each edge location

* Signed URLs and Signed Cookies allow you to control who can access your content. 
    * Signed URLs if you are restricting to individual files. Signed Cookies if you are restricting to multiple files OR dont want to change your current URLs.
* MatchViewer configures cloudfront to communicate with your origin using Http or Https depending on the protocol of the viewer request.
* Create "origin group" for failover for errors and certain http codes.
    * Includes a primary and secondary origin which allows. "origin" in this case means source of information, not origin as in a url origin.  
* Strategies: 
    * geo-restriction - prevents users in specific geographic locations form accessing content that is distributed through CloudFront web distribution.

**Route 53**
* HA and scalable DNS web service.
* Functions: 
    * domain registration
    * DNS routing
    * health checking
* Routing Strategies
    * Latency Routing serves requests from the AWS region that provides the lowest latency.
    * Geolocation routing lets you choose the resources that serve your traffic based on geogrpahic location of your user. 
    * Geoproximity routing serves requests based on geographic location of the user AND the resources they are reaching. 
        * Can also implement a bias which lets you shrink/expand the size of a geographic region from which traffic is routed to a resource
    * Weighted routing lets you choose how much traffic is routed to each resource within a single domain or subdomain.
* Failover routing policy
    * can add a health check on an primary resource and have it failover to a secondary resource when the primary is unhealthy
        * Need to configure NACL and route table to allow 53 to send requests the endpoints specified.  
        * need to enable "Evaluate Target Health" option
* When using Route 53 w/ S3 to serve a static site.  Need to:
    * Setup S3 bucket: 
        * to be configured as a static website.  
        * bucket must have the same name as the domain/subdomain.
    * setup a registered domain name in Route 53
    * Setup Route 53 as the DNS for the domain. 
        * If Route 53 was used to register the domain name, then it is automatically confgured to be the DNS for the domain
* DNS Record Info: 
    * CNAME records are only for subdomains
    * MX records are for mail servers
    * A records are for IPv4 address connections
    * AAAA records are for IPv6 address connections 
    

**Web Application Firewall (WAF)**
* monitors http/https requests
* lets you control access to your content via
    * IP Addresses that requests original from 
    * values in query strings
* Acts in one of these ways: 
    * Allow all requests except the ones you specify => use when CloudFront or ALB serves content but block requests from attackers
    * Block all requests except the ones you specify => serve content for a restricted website whose users are readily identifiable by properties of web request (like their IP addresses)
    * Count the requests that match the properties you specify => allow/block requests based on new props of requests. 
* Integrates w/CloudFront, ALB, API Gateway, and AppSync.  
    * WAF rules run at edge locations so blocked requests are blocked before they get to web servers. 
        * Can create regular rules or rate limit rules.
* Can protect against sql code injection or cross site scripting

**AWS Shield**
* Protects against network and transport layer attacks targetting apps running in EC2, ELB, CloudFront, and Route 53.

**AWS GuardDuty**
* A threat detection service

**AWS Inspector**
* Automated security assessment service that improves security and compliance of applications deployed on AWS 
    * Tests network accessibility of EC2 instances and security state of apps running on those instances.

**AWS Macie**
* Amazon Macie is an ML-powered security service that discovers, classifies, and protects sensitive data stored in S3.


**Amazon Rekognition**
* Service to identify objects, people, text, scenes, and activities

**AWS Directory Service AD Connector**
* Provides multiple ways to use Amazon Cloud Directory and AD with other AWS Services.

**AWS Directory Simple AD**
* Allows management of AD accounts and group memberships, create and apply group policies, and securely connect to Amazon EC2 instances, and provide Kerberos SSO


**AWS Elastic Container Service (ECS)**
* Fully managed Orchestration Service for deployment, management, scaling of container apps.
* Secure environment variables using AWS Secrets Manager or Systems Manager Parameter Store. specify `secrets` w/name of environment variable to pass a secret to a container 
* Docker secrets are not availble in ECS 

**AWS Elastic Load Balancer (ELB)**
* load balances traffic between EC2 instances.

**Network Load Balancer (NLB)**
* receives connection requests and opens a tcp connection on a selected target on the port specified in the listener Configuration
* before application and elastic load balancer
* Can use Bring Your Own IP (BYOIP) feature of an NLB to use trusted IPs as Elastic IP adddresses (EIP)
    * **Note** Cannot use EIP with ALB 

**Amazon Elastic Kubernetes Service (EKS)**
* provisions and scales kuberntes control plane.  
    * includes 
        * api servers
        * backend persistence layer 
    * across multiple AWS AZs
* automatically detects and replaces unhealthy control plane nodes and provides patching for the control plane
* integrated with: 
    * ELB
    * IAM
    * VPC
    * CloudTrail

**AWS Fargate**
* Serverless compute engine for containers
* works with ECS and EKS
    
**AWS Secrets Manager**
* replace hardcoded creds in code with an API call to Secrets Manager
* can configure to auto rotate secrets for you according to a schedule
* manage secrets including: 
    * db creds
    * passwords
    * 3rd party api Keys
    * arbitraty text
* controlled via Secrets Manager Console, Secrets Manager CLI, Secrets Manager API/SDK

**AWS Systems Manager Parameter Store**
* does not rotate its parameters by default

**AWS KMS**
* used to manage encryption keys and control use of encryption across AWS services.
* client gives key to AWS to do encryption.

**AWS CloudHSM**
* managed hardware security module
* allows you to generate and use your own encryption keys
* Keywords: 
    * when you need full control over the encryption of the created key (so not owned or managed by AWS)
    * when you need to audit key usage independently of AWS CloudTrail
* **Note** each custom key store is a ssoicated with an AWS CloudHSM cluster in your AWS account
* Key use cases:
    * You might have keys that are explicitly required to be protected in a single-tenant HSM or in an HSM over which you have direct control.
    * You might have keys that are required to be stored in an HSM that has been validated to FIPS 140-2 level 3 overall (the HSMs used in the standard AWS KMS key store are either validated or in the process of being validated to level 2 with level 3 in multiple categories).
    * You might need the ability to immediately remove key material from AWS KMS and to prove you have done so by independent means.
    * You might have a requirement to be able to audit all use of your keys independently of AWS KMS or AWS CloudTrail. 

**S3**
* Can only add 1 SQS or SNS at a time to S3 events
* Client Side Encryption can be done using AWS KMS Managed Customer Master Key  & Client Side Master Key.  
    * Client Side means client encrypts it before it gets to AWS
* Pre-signed URLs have expiry dates
* Versions
    * standard - is low-latency and provides high-troughput
    * infrequent access (ia) - use data accessed less frequently but requires rapid access when needed (long term storage, backups, and data store for DR)
    * intelligent tiering (it) - automatically moves data to the most effective access tier without operational overload
    * glacier - use for archiving    
* To run simple SQL queries against a subset of data from a specific S3 Object use **S3 Select**
* Encryption
    * Types: 
        * Use Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3)
            * AWS manages both data key and master key.
            * must include header: x-amz-server-side-encryption
        * Use Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)
            * AWS manages data key and you manage master key
            * KMS is the handoff of the MasterKey to the client
        * Use Server-Side Encryption with Customer-Provided Keys (SSE-C)
            * You manage both data key and master key 
            * x-amz-server-side​-encryption​-customer-algorithm
            * x-amz-server-side​-encryption​-customer-key
            * x-amz-server-side​-encryption​-customer-key-MD5

**Amazon Athena**
* Allows you to perform queries against contents of an S3 bucket

**CloudWatch**
* Monitors CPU, Network, Disk perf, Disk Read/write
* To monitor memory, disk swap, disk space, page file, log then you need to create a custom metric.
    * Requires installing CloudWatch agent on EC2 instances to extend the functionality.
* CloudWatch Events can control Elastic Container Service (ECS) Tasks directly (increase/decrease task count).
* CloudWatch Alarms can automatically stop, terminate, reboot, recover EC2 instances.

**CloudTrail**
* Log any activity made in Console, SDKs, CLI and other services. Logs mgmt and data events.
    * By Default: 
        * CloudTrail only monitors log mgmt eevnts.
        * Applies to all regions in the AWS partition in which you are working.
    * To add global services use --include-global-service-events Parameter
    * To add monitoring trail globally --is-multi-region-trail

**AWS ACM**
* Service that lets you provision, manage, deploy public/private SSL/TLS certs for use with AWS services

**AWS Storage Gateway**
* Allows you to interface with S3 using networking protocols (NFS or SMB).  
* Storage File Gateway allows you to integrate on-prem network with AWS.  
* Use when there are no plans to deprecate on-prem infrastructure.
* NOT suitable for transferring large datasets

**Tape Gateway**
* enables you to replace using physical tapes on-prem with virtual tapes in AWS (S3 standard, glacier, deep archive) w/o changing existing backup workflows.

**Internet Gateway**
* used to communicate to the internet from a VPC or subnetwork

**AWS DataSync**
* Simple and Fast to move large amounts of data between on-prem and S3/EFS/FSx
* use to
    * migrate active data to AWS
    * transfer data for analysis/processing
    * archive data to free up on-prem storage
    * replicate data to AWS for business continuity

**AWS Glue**
* Fully managed extract, transform, and load (ETL) service that is used for preparing and loading data for analytics.

**FSx**
* Fully managed file system for Windows and has AD integration
    * FSx for Lustre is high performance file system 

**EFS**
* Fully managed file storage service that makes it easy to setup and scale file storage in the Cloud. 
* supports file locking
* **Note** ONLY SUPPORTS LINUX

**API Gateway**
* Will automatically scale and handle massive traffic spikes BUT you still need to configure throttling to further manage bursts

**AWS Global Accelerator**
* Networking service that simplifies traffic mgmt and improves app perf.  
* Dont use for general HTTP. 
* Use for UDP(gaming), MQTT (IoT), Voice over IP, or http that specficially require static IP addresses or deterministirc, fast, regional failover

**AWS Resource Access Manager (RAM)**
    * Enables you to securely share AWS resources with any AWS account or within your AWS Organization.  

**AWS Organizations**
    * is an acct mgmt service to consolidate multiple AWS accounts.

**AWS Control Tower**
    * built on top of AWS Organizations. 
    * Setup environment and set guardrails and use Organizations to create custom policies that control AWS services and resources across multiple AWS accounts.

**Amazon EMR**
* managed cluster platform that simplifies running big data frameworks (i.e. Hadoop/Spark) on AWS to process and analyze vast amounts of data.
* can transform and move large amounts of data in/out of other AWS data stores and databases
* Question Key Words: big data processing frameworks

**RDS**
* Relational managed database
* Enhanced Monitoring gives you metrics from the db agent on the instance so it's more accurate thatn CloudWatch.
* Events are limited to DB Instance events.  
    * **Note** To check for data-modifying events, you need to use native functions or stored procedures.
* Fails over automatically
    * When failing over, RDS flips the CNAME of the DB instance to point to the standby RDS instance and then promotes that instance to primary.

**DynamoDB**
* NoSQL managed database
* fully managed
* Stream is enabled, it produces an ordered flow of information about changes to items.
* DAX - accelerate read performance from milliseconds to microseconds

**Aurora**
    * To load balance reads/writes use custom endpoints.  
    * Custom endpoints 
        * Create an endpoint that is pointed just to the master db and another endpoint that is pointed at the read replicas.  
            * Example: So if you have a reporting/help-desk dashboard it could point to the read replicas alone whereas a primary application can point to the writing db

**Amazon Redshift**
* Used as a data warehouse
* Spectrum - enables you to query and analyze all of your data in S3 using open data formats with no data loading or transformations
* Sharding
    * shard iterator
        * returned by GetRecords request
        * expires: 
            * If Dynamo DB table used by Kinesis does not have capacity to store lease data
                * can increase write capacity to the shard table to resolve this
            * 5 minutes 
            * when you restart your app
* Question Key Words: big data processing, various BI tools and standard SQL queries

**Amazon Kinesis Platform**
* Collects, processes, and analyzes streaming data in real time
    * uses DynamoDB to store data as it streams
* Kinesis Connector - 
* Kinesis Data Streams - an application that you use to collect and process larges steamd of data records in real time. 
    * use Kinesis client library
    * runs on EC2
* Kinesis Data Firehose - fully managed service for delivering real-time streaming data to S3, Redshift, OpenSearch Service, Splunk, custom http endpoint   
    * can transform data before sending it 
* Kinesis Video Streams - fully managed service to stream live video from devices to AWS or build apps for real-time video processing or video Analytics
    * can store mediate data for a specified retention period (default encrypted at rest)
* Kinesis Data Analytics - allows you to run SQL against streaming data to perform time-series analytics, feed real-time dashboards, create real-time metrics
    * uses kensis data streams and kinesis firehose as streaming sources

**Redis**
* Use as a distributed session management.  
* To secure the session data from manipulation, you can runa  REDIS Cluster with the --transit-encryption-enabled and --auth-token parameters enabled.  
    * --auth-token parameter will make it a requirement to enter your password when connecting to the Redis server

**AWS X-Ray**
* Helps debugging & analyzing Microservices apps with request tracing so you can find root cause issues

**Amazon Elastic File System(EFS)**
* Max lifecycle policy of 90 days.

**Security Groups**
* Control Traffic to EC2 instances
* VPC can only be secured via Security Groups
* Security groups only have inbound rules.  
    * All inbound rules are duplicated for outbound (if you allow incoming on port 80 then it auto allows outgoing on port 80)

**Network ACL (NACL)**
* NACLs control traffic to VPC subnets.  
* NACL has both inbound and outbound rules.

**SQS vs SNS vs Amazon MQ**
    * All support messaging 
    * Use SQS/SNS if its a new application
    * Use MQ if migrating an existing on-prem messaging platform that uses standard protocols

**SQS**
* used as a queue for messaging
* max retention day for messages is 14 days
* can contain unlimited number of messages

**SES**
* Use for notification and transactional emails

**SNS**
* Provides pub/sub functionality via topics.
* Use to send emails when you want to monitor your EC2 instances

**Notes**
* SSH uses TCP over port 22

**VPC**
* Enable access to network from VPC
    * Attach virtual private Gateway to VPC
    * create a custom route table
    * update security group rules allowing traffic
    * create AWS managed VPN connection (VPN here means connection between VPC and client network)
        * To create a VPN connection, need to create a **Customer Gateway Resource** in AWS.
* Endpoint - allows private connection between VPC and AWS services and other VPC encpoints (for other VPC comm, it uses AWS PrivateLink)
    * Can create endpoint policy to control access to the service that the endpoint is connecting to
* Subnet - range of IP Addresses 
    * Must specify a range of IPv4 addresses in CIDR notation
    * Can optionally add IPv6 addresses range
    * DualStack Mode is where your resources can communicate over IPv4, IPv6, or both but not IPv6 exclusively.
* Peered connections are NOT pass through connections.  
    * If VPC A and VPC B are peered and VPC A has access to a VPN that connects it to a corporate network.  THat does NOT mean that VPC B can access that corp network. 
* **Note** IPv6 addresses are public and reachable over the internet generally.  IPv4 addresses are NOT.  So you can associate a IPv6 block with VPC and subnets if you want them to be publicly accessible

**AWS Config**
* enables you to assess, audit, and evaluate configs of your AWS resources.  
* continuiously monitors and records your AWS resource configs 

**AWS Trusted Advisor**
* provides best practice recommendations

**AWS OpsWorks**
* Configuration management service that provides managed instances of Chef and Puppet.  
* Lets chef/puppet automate how servers are configured, deployed, managed across EC2 instances and on-prem compute environments.

**AWS Beanstalk**
* handles application deployment details (capacity provisioning, load balancing, auto scaling, app health monitoring)

**AWS CloudFormation**
* lets you create a collection of related AWS resources andprovision them in a predictable fashion using infrastructure as code.

**Amazon Simple Workflow Service (SWF)**
* fully managed state tracker and task coordinator.
* is a web service
* used to build applications that use AWS to coordinate 

**AWS Security Token Service (STS)**
* allows you to create and provide trusted users with temp security creds that can control access to your AWS resources

**AWS Cognito**
* used for user authentication 

**AWS SSO**
* cloud SSO taht centrally manages SSO access to multiple AWS accounts and business applications
* uses STS

**Data Transfer Options**
* Snowball - if it takes more than one week to upload your data to AWS then use Snowball.
    * if you need secure and quick transfer of terabytes to many petabytes from on-prem to AWS.
    * if you dont want to make expensive upgrades to your network
    * if you frequeently experience large backlogs of data
    * if youre located in a physically isolated environment
    * if you dont have high speed internet
* Snowball Edge - can undertake local processing and edge-computing workloads in addition to what's available in regular Snowball. 
* Snowmobile - if you need to move EXTREMELY large amounts of data (up to 100 Petabytes of data)

**Bastion Host**
* EC2 on a network specifically designed and configured to withstand attacks
* should be in public subnet with either a public/elastic IP address 
* should be configured to have RDP or SSH access defined in the security group for the subnet it's in. 