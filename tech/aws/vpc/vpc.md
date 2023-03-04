# VPC

## Key Takeaways: 
* Think of them private data centers (as opposed to private networks because vpcs allow access to services and hardware and stuff)


## Key Features: 
* VPC Endpoints
    * highly available and highly redundant and scalable virtual devices
    * two types of endpoints: 
        * gateway endpoints
            * places a route in a routing table to provide access between endpoints
            * high speed secure AWS services            
            * used for access to dynamo or S3
                * allows private access from VPC to S3
                * creates a prefix list in addition to endpoint on S3 and VPC
                    * prefix list has a naming convention: pl-xxxxxx
                * routing table will show route/prefix
                * route tot he vpc endpoint will be in 
            * policies can be setup to limit resources that are avaialble from the endpoint
            * limit routing information to subnets that need access to the endpoint
                * if you dont have a route in the route table, you cant reach it.
        * interface endpoints
            * uses AWS Private Link to connect
                * Virtual private line over the AWS network
                * private link creates an ENI (elastic network interface)
                * restricts all traffic between the VPC and the AWS/Customer/Partner organization
            * connect AWS services and external organizations or different vpcs
            * these are local to the VPC
            * effectively are an elastic network interfact in yoru VPC
            * when its created, endpoint AWS generates an AWS endpoints specific DNS name so that you can connect to the endpoint via DNS name


## Notes
* VPC Peering vs Private Link
    * Private link allows access to a very specific services
    * VPC peering allows access to all the services that you allow
    * VPC peering allows a moderate number of connections (125)
    * Private link is scalable
    * limites are based on max load balancer throughput  and servers
    * Private link solves the address problem when connecting to external vpcs
    * Private link uses NAT so there is no need to worry about overlapping address space
