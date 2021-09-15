# Networking

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