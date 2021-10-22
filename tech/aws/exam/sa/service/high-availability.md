# High Availability

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