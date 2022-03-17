# Performance


## Caching
* Reverse Proxy Cache in front of web server
* Users -> Edge Locations (AWS CloudFront) -> Web -> App -> DB
*  **AWS CloudFront** - Caching
    * Supports WebSocket
    * How to setup: 
        * Configure Origin: S3, WebServer
        * Create a CloudFormation distribution which tells CloudFront which origin servers to get your files from when users request the files through your website/applications
        * CloudFront assigns a domain name to your new distribution
        * CloudFront sends your distribution's configuration but not the content to all of its edge locations.  
    * How to expire contents
        * Assign TTL 
        * Change the Object name
        * Invalidate the object (VERY inefficient)
    * When drawing architechtural diagram, make sure cloudfront shows up OUTSIDE the region
    * **Questoin** - How does it manage permissions

**AWS Web Application Firewall (WAF)**
* Stands this up in front of the Amazon CloudFront to protect from DDos attacks

**Session Management**
* Store session infomration in DyanmoDB DAX (DynamoDB Accelerator) (Session States)
    * DAX is a caching mechanism for DynamoDB
* Amazon ElastiCache - 
    * Strategy
        * Write through
            * Will write to Elasticache first and then to DB so that Elasticache is always up to date
        * Lazy Loading
            * On Cache miss from Elasticache, read from db, write back to elasticache
    * Adding TTL
        * A TTL value is added to each app write to elasticache
        * When the TTL Expires the app will query the database for data
    * Elasticache Options: 
        * Memcache 
            * can scale up to 20 nodes per cluster
        * Redis
            * Can scale up to 90 nodes