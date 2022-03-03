# EC2

## Unorganized

* Is there a difference in cost/updtime/performance between FSx and S3?
    Yes 
* Is there any time you would choose FSx over S3 if theres only one instance using it?
    S3 is way cheaper so no, unless there is potentical for multi instance use later on
* For spot instances is there a guarantee time before fulfill? 
    * use [EC2 Spot Blocks](https://aws.amazon.com/blogs/aws/new-ec2-spot-blocks-for-defined-duration-workloads/) to guarantee a spot instance that will last a specific amt of time
* If you have auto-assign EC2 Public IP - does that change on shutdowns or is that a permanently tied public IP?
    * Yes, but you can use an Elastic IP to get a permanent IP for that instance
* If you first created an instance without a keypair, can you come back later and add one?
    * Yes you can 

EBS vs S3 vs EFS/FSx
    * If multiple instances need to use the same storage 
        * EBS only attaches to one instance
        * S3 is an option but not ideal
        * Amazon EFS (Elastic File System for Linux)/FSx (File System for Windows)
            * sipmle scalable file storage 
            * shared across AZs/Regions/VPCs/Accounts         

## Basics
* Need fulfilled: Running applications that are going to be used consistently but by a small number of users
* Hardware
    * Chip types: all xeon
        * Intel AES-NI - enables encryption 
            * Includes Threat detection technology
        * Intel AVX (Advanced vector extension) - 512 bit encryption. improve floating point performance.  Only avaialble
    * Features of chips
        * Intel Turbo Boost - runs corse faster when needed
        * Intel TSX  - uses multiple threads dynamically             
        * P state and C State - fine tune performance and sleep state of each corse
        * DLB (deep learning boost) - embededd performance for AI workloads.  Up to 30x performance improvement
* Uses
    * Web hosting
    * Databases
    * authentication
    * anything a server can do
* Naming convention
    * m5.large
        * m is the family name
            * A, T, M - general Purpose
                * Burstable workloads for website/web applications
            * C - compute optimiszed
                * High performance computing, scientific modeling, batch processing, deep/machine learning
            * R, X, Z - memory Optimized
                * In memory databses, in memory cache, application/real-time performance optimized, 
            * P, Inf, G, F - Accelerated computing
                * Maching and Deep Learning - Way more powerful than Compute
            * I, D, H - Storage Optimized
                * Data processing, big data, distributed file systems
        * 5 is generation number
        * large shows server size
* Pricing (ordered from most to least expensive)
    * Dedicated instance/host - used for compliance or security requirements are high
        * Isolated at hardware level
        * instance - runs on a specific piece of hardware
        * hosts - same as instance except you get to choose the type of hardware - full physical server with EC2 insance capacity fully dedicated to your use
    * On-demand
        * no long term commitment
        * no upfront payments
        * increase/decrease compute capacity depending on deamnds of application
        * CONS: Expensive.  Use when starting out but use Reserved once you know what youre building
    * Reserved (commit to using between 1-3 years)
        * per pay for capacity
        * Standard RI, Convertible RI, Scheduled RI
            * Standard - use all the time
            * Convertible - can change its configuration while youre using it
            * Scheduled - can schedule when you are going to use it
        * 3 Upfront payment methods
            * Full upfront payment
            * partial upfront 
        * Can be shared between multiple accounts (within a billing fmaily)
        * Need to commit to at least 1 year
    * Savings Plan
        * Compute savings plans provide flexibility to help reduce costs
        * Apply to a specific instance family within a region and provide the largest discount (up to 72% in savings)
    * Spot intances
        * Purchase unused EC2 capacity
        * Interruption notice provided 2 minutes prior to instance termination
        * flexibility is key to success
* Key Considerations
    * does your compute layer require lowest latency/highest packet-perp-second network perofmrance?
        * use cluster placement groups 
            * groups multiple instances within a signel AZ
            * launch all instances at one time.   
        * spread placement group
            * purposely positioned on distinct hardware. can span multiple AZs (max of 7 per AZ per group)
        * partition placement group
            * large disributed and replicated workloads (HDFS, HBase, Cassandra running on EC2s)

* Key Components
    * Tools: 
        * AWS Compute Optimizer - recommends optimal AWS Compute resources for workloads to reduce costs and improve performance by using machine learning to analyze historical utilization metrics
    * AMI - Amazon Machine Image
        * EC2 Image Builder - Tool that simplifies creation, maintenance, validation, sharing and deployment of LInux and Windows server images
        * Uses: Great for Repeatabilty creating same environment, recoving an environment, backing up environments
        * Contains:
            * 1 or more EBS volumes
            * A template for the root volumes
            * Launch permissions
            * A block device mapping (can specify volumes to be attached when launched)
        * Where to find: 
            * Pre-Built
            * AWS Marketplace
            * Create your own (setup your own EC2 manually and create an AMI from that)
    * Launching an EC2 instance with scripts upon creation (BASH and Powershell scripts)
    * **TEST QUESTION** Retrieving EC2 Instance with instance metadata: 
        * http://<ip>/latest/meta-data/public-hostname
    * Storing data 
        * Amazon EBS - Elastic Block Store 
            * Use cases
                - when an application needs block level storage 
                - persists data through shutdowns 
                - need to be able to backup data
                - **NOTE** - only attaches to one instance
            * Volume TYPES
                * Solid State Backed
                    * General Purpose SSD - used for most workloads
                    * Provisioned IOPS SSD - critical business applications that required sustained IOPS performance or LARGE database workloads
                * Hard Disk Backed
                    * Throughput Optimized HDD - streaming workloads, big data, data warehouses, log processing, cannot be a boot volume
                    * Cold HDD - throughput oriented **NOT FINISHED**
            * Instances optimiszed for EBS
        * Instance Store - used for temporary storage (ephemeral data - data that is only available until the instance is stopped)
