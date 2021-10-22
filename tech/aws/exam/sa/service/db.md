# Databases

* Need fulfilled: creating a data store that is HA and easy to scale 
* Considerations
    * Scalability - how much throughput
    * Storage requirements - GB, TB, or PB
    * Object Size and type - Store simple data structures or lrage data objects or both
    * Durability - availability/recoverability.  
* Types
    * relational: SQL, Oracle, MySQL, AWS RDS, AWS Redshift, AWS Aurora
        * Strict schema rules
        * doesnt need extreme read/Write
        * does not require extreme performance
    * Nonrelational: Mongo, Cassandra, AWS Dynamo, AWS Elasticache, AWS Neptne
        * no set schema.  key/value pairs, documents, graphs
        * scales horizontally
        * read/write really high
    * **TEST** - RDS vs Dynamo
        * RDS
            * Just a DB Service for relational dbs, not a DB itself.  Under RDS Service you can run 6 different Relational Databases
            * fully managed relational DB
            * provisions new instances in minutes
            * scaling vertically in a few mouse clicks
            * AWS Aurora - DB Engine that works with RDS 
                * 5x throughput of MySQL
                * 3x througohtpu of PostgreSQL
                * Replicatdes 6 ways across 3 AZs
                * Requires very little change to existing application
                * Automatic fail over 
            * Security Controls
                * access is to table level
                * encrypted at rest
                * encrypted in transit
                * event notifications about db instance
        * Dynamo
            * Fully managed non relational DB
            * event driven programming (serverless computing)
            * extreme horizontal scaling capability
            * Connected to Lambda
            * Option of Eventually Consistent vs Strongly Consistent
                * Eventually has the potential for stale reads
                * Strong - pulls the latest write
            * Security Controls
                * Definable access permissoins - can go down table, item, or even attribute level
                * Encryption at rest 
                * SSL/TLS communication 
        * Migrate data into AWS database
            * AWS DMS - Tool to use most of the time
                * supports migration to and from most commercial and open source dbs 
                * can be used to migrate btwn databases EC2, RDS, S3 and on prem
                * can perform one-time migration OR ongoing migration
                * source db doesnt have to go down to do the transfer
            * AWS Snowball Edge - Tool to use if too much data or bad connection or security concern

* Managed vs Unmanaged
    * Managed - 
        * just need to worry about app performance
    * Unmanaged - 
        * AWS takes care of OS, Server maintnence, rack/stack, power, hvac, net
        * You need to worry about app perf, scaling, HA, DB Backup, DB patches/installs, OS Patches

