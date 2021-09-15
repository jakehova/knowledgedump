# Basics 

## AWS Data Centers
* all sites are online
* grouped by availability zones (AZ)
    * 81 AZs
    * made up one or more data Centers
    * designed for fault isolation
    * interconnected with other AZs using high-speed private links
* grouped AZs are Regions
    * 25 regions worldwide (there are 2 gov cloud regions east/west)
    * enable and control data replication across regions
    * communication between regions uses AWS backbone network infrastructure
* edge locations
    * 200+ edge locations
    * act similar to CDNs as cache points run on cloudfront 

## Tags
* [Best Practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf)
* Each tag has a key/value pair
* Use to categorize resources (generally include a baseline of version, dns name, environment, app stack, purpose, owner)
* Standardize, case sensitive format for Tags
* implement automated tools to help manage resource Tags
* favor using too many tags rather too few

## Tools
* [Simple Cost Calculator](https://calculator.s3.amazonaws.com/index.html)
* [Architechture day to day operations help](https://aws.amazon.com/architecture/) 
* [Tool to generate well archtected architecture](https://aws.amazon.com/well-architected-tool))
* [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
* [AWS Architechture Icons](https://aws.amazon.com/architecture/icons/)