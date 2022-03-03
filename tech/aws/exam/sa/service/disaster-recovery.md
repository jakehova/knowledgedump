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
    