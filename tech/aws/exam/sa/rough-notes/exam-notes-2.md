# Exam Notes



**VPC communication**
* AWS Transit Gateway connects your VPC to on-prem networks through a central hub
* AWS Direct Connect establishes a dedicated network connection from on-prem to AWS
* AWS VPN CloudHub is used to provide secure communication between remote sites 
* VPC endpoint without leaving AWS (private connection) then use VPC Endpoint

**EC2**
* During Scale-In, default termination policy is to remove the instance with the oldest configuration. 
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
    * Simple Scaling - waits for a cool down period (default to 300 seconds) to expire before spinning up the next instance
        * Target Tracking Scaling - increases or decreases instances based on the target value of a metric.  Scales out or in to keep as close to target value of metric as possible
        * Scheduled Scaling - scales based on predicted patterns
        * Suspend/Resme Scaling - temporarily pauses scaling activities
* Metadata
    * Instance metadata - data about your instance that you can use to configure/manage running the instance 
        * Instance ID
        * Public IP
        * Public Keys
    * User Data - used to perform common automated config tasks and run scripts after the instance starts
    
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

**Network Load Balancer**
* routes traffic to targets
* does NOT support path-based routing or host-based routing

**Classic Load Balancer**
* use for aps that are built within the EC2-Classic network only.
* does NOT support path-based routing or host-based routing

**Gateway Load Balancer**
* used for deploying, scaling, and running 3rd party virtual appliances.  
* does NOT support path-based routing or host-based routing

**CloudFront**
* Signed URLs and Signed Cookies allow you to control who can access your content. 
    * Signed URLs if you are restricting to individual files. Signed Cookies if you are restricting to multiple files OR dont want to change your current URLs.
* MatchViewer configures cloudfront to communicate with your origin using Http or Https depending on the protocol of the viewer request.
* Create "origin group" for failover for errors and certain http codes.
    * Includes a primary and secondary origin which allows. "origin" in this case means source of information, not origin as in a url origin.  
* Strategies: 
    * geo-restriction - prevents users in specific geographic locations form accessing content that is distributed through CloudFront web distribution.

**Route 53**
* Routing Strategies
    * Geolocation routing lets you choose the resources that server your traffic based on geogrpahic location of your user. 
    * Weighted routing lets you choose how much traffic is routed to each resource within a single domain or subdomain.

**WAF**
* Integrates w/CloudFront, ALB, API Gateway, and AppSync.  
    * WAF rules run at edge locations so blocked requests are blocked before they get to web servers. 
        * Can create regular rules or rate limit rules.

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


**AWS ECS**
* Fully managed Orchestration Service for deployment, management, scaling of container apps.
* Secure environment variables using AWS Secrets Manager or Systems Manager Parameter Store. specify `secrets` w/name of environment variable to pass a secret to a container 
* Docker secrets are not availble in ECS 

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
* Encryption
    * Server-Side
        * Managed Encryption (SSE-S3), request must include header: 
            * x-amz-server-side-encryption
        * Customer Encryption (SSE-C), request must include headers:
            * x-amz-server-side​-encryption​-customer-algorithm
            * x-amz-server-side​-encryption​-customer-key
            * x-amz-server-side​-encryption​-customer-key-MD5

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

**AWS DataSync**
* Simple and Fast to move large amounts of data between on-prem and S3/EFS/FSx
* use to
    * migrate active data to AWS
    * transfer data for analysis/processing
    * archive data to free up on-prem storage
    * replicate data to AWS for business continuity

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

**AWS Resource Access Manager (RAM)**
    * Enables you to securely share AWS resources with any AWS account or within your AWS Organization.  

**AWS Organizations**
    * is an acct mgmt service to consolidate multiple AWS accounts.

**AWS Control Tower**
    * built on top of AWS Organizations. 
    * Setup environment and set guardrails and use Organizations to create custom policies that control AWS services and resources across multiple AWS accounts.

**RDS**
* Relational managed database
* Enhanced Monitoring gives you metrics from the db agent on the instance so it's more accurate thatn CloudWatch.
* Events are limited to DB Instance events.  
    * **Note** To check for data-modifying events, you need to use native functions or stored procedures.

**DynamoDB**
* NoSQL managed database
* Stream is enabled, it produces an ordered flow of information about changes to items.

**Aurora**
    * To load balance reads/writes use custom endpoints.  
    * Custom endpoints 
        * Create an endpoint that is pointed just to the master db and another endpoint that is pointed at the read replicas.  
            * Example: So if you have a reporting/help-desk dashboard it could point to the read replicas alone whereas a primary application can point to the writing db

**Amazon Redshift**
* Spectrum enables you to query and analyze all of your data in S3 using open data formats with no data loading or transformations

**Amazon Kinesis**
* Collects, processes, and analyzes streaming data in real time.
* Kinesis Data Firehose - fully managed service for delivering real-time streaming data

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
* Security groups only have inbound rules.  
    * All inbound rules are duplicated for outbound (if you allow incoming on port 80 then it auto allows outgoing on port 80)

**NACL**
* NACLs control traffic to VPC subnets.  
* NACL has both inbound and outbound rules.

**SQS vs SNS vs Amazon MQ**
    * All support messaging 
    * Use SQS/SNS if its a new application
    * Use MQ if migrating an existing on-prem messaging platform that uses standard protocols

**SES**
* Use for notification and transactional emails

**SNS**
* Provides pub/sub functionality via topics.
* Use to send emails when you want to monitor your EC2 instances

**Notes**
* SSH uses TCP over port 22


