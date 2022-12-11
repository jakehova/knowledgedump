# DMS

## Process
* Create Replication Instance -> Create Endpoint for Source 

## Types
* Homogenous - same db for source and destination
* Hetereogenous - different db for source and destination

## Replication Instance
* Sits between source/destinating dbs
* pulls data from source db, does any necessary modifications of data to make data proper type/structure in destination db, moves data to db
* publishess logs and monitoring statistics
* Does: 
    * initial load of data
    * can handle ongoing replication of changes
* Right Sizing
    * Understand replication workload
        * # of incoming changes
        * sorter - task that runs on instance. filters data from soruce to what data needs to go to destination and prepares the order for how those changes are to go to destination
        * # of outgoing changes
        * instance type: 
            * R: high txs per second
            * T: light workloads and testing
            * C: Compute intensive, good for heterogenous migrations

## Configuring Endpoints
* Sources & Targets
        * Endpoint Identifier - This is an endpoint label
        * Source Engine Selection
        * configure connection details
        * optional endpoint settings/attributes
* Best Practices
    * Check requirements (verify type and version)
    * Plan for incompatible Types
    * Verify engine settings: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html

## Replication task
* Replication Task ties the Endpoints to a Replication Instance
* Task Configuration
    * Task Identifier
    * Select Replication Instance
    * Source & Target Endpoint
    * Migration Types
        * 1 time migration 
        * Migrate existing data and replicate ongoing changes
        * Replicate new changes only 
* Task settings
    * Target table preparation mode
        * Do Nothing - doesnt touch tables if they already existing
        * Drop tables on target - drop tables on target if they already exist/creates new tables on target and migrates/replicates data
        * Truncate - leaves tables or creates them on target, 
    * Large Object (LOB) Column Handling
        * dont include 
        * full mode - include everything
    * Logging Options
    * Advanced Task settings
* Premigration Assessment (optional)
    * Check for potential migration issues
* Migration Task Startup
    * Behavior (Automatically or Manually)