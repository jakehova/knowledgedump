# VPC

* VPCs are deployed at region level
* **VPC Peering** - connecting two VPCs
    * No transitive communication.  If VPC A is peered to VPC B and VPC B is peered to VPC C.  VPC A cannot communicate with VPC C
    * Ensure that there ar no overlapping CIDR blocks
    * Only connect essential VPCs
    * Make sure your solution can scale 
* **Transit Gateway** - connects up to 5000 VPCs and On-premise environments to a single gateway
    * Acts as a hub for all traffic to flow thorugh between your networks
    * Fully managed, HA, flexible routing service
    * Allows for multicast and inter-regional peering
    * Connect a VPC to a Transit Gateway by updating the VPC Routing Table with the Transit Gateway destination and vice versa
    * Create 1 route table for incoming (external to business network) and 1 route table for outgoing (from vpc to external)
* private network space in the AWS cloud
* provides logical isolation for your workloads
* allows custom access controls and security settings for your resources
* requires an ipv4 address space and optionally ipv6 address ranges
* enables you create specific CIDR ranges for your resources (usually done through subnet)
* provides strict access rules for inbound/outbound traffic
* For most use cases there are 2 primary patterns for organizing infrastructure
    * Multi-VPC
        * Single team or single org such as managed service providers
        * limited teams, which makes it easier to maintain standards nd manage access
        * CON: governance and compliance standards are more difficult to manage
    * Multi-Account
        * large orgs and orgs with multiple IT teams
        * medium sized orgs that anticipate rapid growth
* Can have multiple VPCs in the same region (up to 5 per region)
* each VPC reserves a range of private IP addresses
* private IPs can be used by resources deployed into that VPC
* ip range is defined using classeless inter-domain routing (CIDR)
    * 10.0.0.0/16 = all IPs from 10.0.0.0 to 10.0.255.255 **QUESTION: NO IDEA HOW CIDR WORKS**
        * 10.0.0.0/8 = all IPs from 10.255.255.255
        * 10.0.0.0/32 = 10.0.0.0 (only one IP address)
        * 10.0.0.0/0 = broadcast
        * 10.0.0.0/24 = 10.0.255.255
        * /28 = 16 IPs, /20 = 4096 IPs
    * an IP 
    * 32 is max CIDR
    * first two numbers (from the left) are fixed
    * the last 2 numbers are used for the range of IP addresses
* supports bringing your own IP prefixes
* **Subnet** - segment of partition of a VPCs IP address range where you can isolate a group of resources
    * subset of VPC CIDR block
    * Subnet CIDR blocks cannot overlap
    * Each Subnet resides entirely within one AZ
    * an AZ can contain multiple multiple subnets
    * AWS will reserve 5 IP addresses from each subnet 
    * public subnet
        * include a routing table entry to an internet gateway to support inbound/outbound access to public internet
    * private subnet
        * do not have a routing table entry to an internet gateway
        * are not directly accessible from public internet
        * typically use a NAT gateway to support restricted, outbound public internet access
            * create a NAT Gaeway in public subnet and private subnet should have access NAT gateway
        * Private subnet traffic goes to NAT gateway goes to AWS internet gateway
* **Internet Gateway** 
    * allows comm betwen instances in your VPC and interne
* **NAT Gateway**
    * enable instances in the private subnet to initiate outbound traffic to the internet or other AWS Services
    * prevent private intsnaces from recevingin inbound traffic
* **Route Table:** helps direct traffic between VPC resources
    * Each VPC has a default route table
    * you can create custom route tables
    * all subnets must have an associated route table
    * BEST PRACTICE: Use custom route tables for each subnet 
* Best Practices: 
    * Consider large subnets over smaller ones (/24 and larger (which means smaller number))
        * simplifies worload replacement
    * In each AZ you have at least one private and one public subnet
    * whenever youre allocating IPs, reserve more for priavte than public
* **ENI - Elastic Network Interfaces**
    * virtual network interafce that can be moved across EC2 instances in the same AZ
    * when moved maintains private IP addresses, elastic IP address, public IP address
    * max of 5 per region

VPC 10.1.0.0/16
Inbound Traffic goes through internet gateway -> VPC -> then route table -> network ACL -> Subnet -> security group - EC2 Instance
Outbound traffic is the reverse

## Security Group
* Virtual firewalls that control inbound/outbound traffic into AWS resources
* Traffic can be restricted by any IP protocol, port, or IP address
* Rules are stateful (info about the connection including port is always tracked)
* The default security group, blocks all inbound and allows all outbound
* BEST PRACTICE: Create a security group per functional tier (i.e. for web layer, app layer, db layer should each have their own SG)
* Network ACL
    * firewall at subnet boundary
    * allow all inbound and outbound by default
    * stateless requiring explicit rules for both inbound/outbound traffic
