# Well Architected Framework



## Pillars of Well Architechted Framework
**Security**
* [Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
* Identity Foundation (principle of least privelage and seperation of duties)
* Enable traceability (monitor, alert, audit, and log actions)
* Security at all layers
* Risk assessment and mitigation strategies
**Reliability**
* dynamically acquite computing resources to meet demand
* recover quickly from infrastructure or service failures
* mitigate disruptions due to misconfiguration and transient network issues
**Cost Optimization**
* Measure Efficiency
* Eliminate Unneeded expenses
* Consider using manageed services (dont have to worry about setting up/managing/maintaining servers)
**Operational Excellence**
* ability to run and monitor systems
* continually improve supporting process and procedures
**Performance Efficiency**
* choose efficient resources and maintain their efficiency as demand changes
* democratize advanced technologies
* mechanical sympathy (use best tech for the job)

## Choosing regions for Architechture
    * Data residency and regulatory compliance (each region )
        * Are there relevant region data privacy laws
        * can customer data be stored outside the country
        * can you meet your governance obligation
    * Proximity of users to data
    * Service & feature availability
        * some services are not available in all regions
        * can use SOME services cross region but at increased latency
        * services expand regularly
    * Cost effectiveness
        * costs vary by region
        * some services like S3 have costs for transferring data out
        * consider the cost-effectiveness of replicating the entire environment in another region
