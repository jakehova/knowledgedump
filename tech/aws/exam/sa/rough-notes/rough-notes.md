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

# SNS/SQS
* Problem: Web Tier and App Tier are tightly coupled.
    * Solution 1: Put Elastic Load Balancer (ELB) in between web and app tier.  Issue with this is that if there are any network issues, use queueing
    * Solution 2: Use SQS 
**SQS**
* Pros
    * Fully managed queuing service
    * Messages are stored until they are processed and deleted
    * Acts as a buffer between senders and receivers
* Types
    * Standard Queue: At least once delivery
        * Messaging Limit: Nearly unlimited
    * FIFO Queues: Messages are processed exactly once in the exact order
        * Messaging Limit: 300 Messages a second 
* Features
    * Persists Messages
    * Long Polling
    * Send/receivers
    * One to One
    * Dead Letter Queue (DLQ): Move messages that cant be processed to this queue.
    * Visibility Timeout: When a message is pulled off the queue while its not deleted it is made invisible to other processes acting on the queue
    * Long Polling: Reduces costs 
* Message has limitation of 256k
* Process
    1 Producer sends message to queue which gets distributed redundantly
    2 Message gets picked up for processing by consumer and visibility timeout starts
    3 Message gets deleted by consumer after receiving and processing it
**SNS**
* Coordinates and manages messaging between publishers and subscribers
* Subscription Types
    * Email
    * Http/Https
    * SMS
    * SQS
    * Lambda Functions
* Characteristics
    * No message persistence
    * Push 
    * pub/subscribers
    * one to many communication
    * Single Published Message
    * No recall options
    * Http/Https retry
    * Order and delivery not guaranteed
**Amazon MQ**
* When to Use: Using a messaging system with an existing application and want to move the application to the cloud otherwise use SNS/SQS
* Manged message broker service for Apache MQ
* Makes it easy to setup and operate message brokers in the cloud
* Direct access to Active MQ conole
* Compatible with open standard APIs and protocols: JMS, NMS, AMQP, STOMP, MQTT, and WebSocket

    
# Microservices
**Elastic Container Service**
* Container Management Service
* Orchtestrates the execution of containers
* Maintains and scales the fleet of nodes running your containers
* Removes the complexity of standing up the infrastructure
**Fargate**
* Fully managed container service
* Provisioning and managing clusters
* Scaling
* You can run EKS and ECS on AWS Fargate
**Elastic Container Registry**
* Fully managed Docker Container Registry
**Lambda**
* Fully managed compute service
* Runs stateless code
* Can run at edge
**API Gateway**
* Prevents exposing endpoints
* Protection from DDoS and injection attacks
* Host and use multiple versions and stages of your APIs
* Create and distribute API keys to developers
* Leverage signature version 4 to authorize access to APIs
* Integrates with Lambda OR as a VPC endpoint 
**AWS Step Functions**
* Coordinates Microsoervices using visual workflows
* Allows you to step through the functions of your application
* Automatically triggers and tracks each step
* Provides simple error catching and logging if a step fails
* Is a State Machine 

# Disaster Planning/Recovery 
* Recovery Point Objective (RPO)/Recovery Time Objective (RTO)
    * RPO - How often does data need to be backed up
        * Example: Business can recover from losing at most the last 12 hours of data
    * RTO - How long can app be unavailable
        * Example: Application can be down and unavailable for a max of 1 hour
* Storage Backup DR Options
    * **S3**
        * DR - Cross-Region replication
        * Glacier - Data stored in regional vaults
        * EBS - create point in time volume snapshots and copy snapshots across regions and accounts
        * AWS DataSync - 
    * **AWS Backup**
        * Centralized Backup service to backup application data across services
* Networking DR Options
    * **Amazon Route 53** 
        * Traffic distribution
        * Fallover
    * **ELB**
        * Includes load balancing/health checks and failover
    * **Amazon VPC**
        * Extend your on-prem network topology to the cloud
    * **AWS Direct Connect**
        * Fast and consistent backup/replication of your large on-prem env in the cloud
    
# Optimizations
* What do I need right now?
* Can I afford to pay for capacity I'm not really using?
* Are there single points of failure?
* Can it recover from disaster?
* Is it self healing? 
* Are there any tight dependencies? Switch to Microservices

