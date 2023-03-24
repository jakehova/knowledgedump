# Topics

## What are they?
* Named feed or category of messages
* Logical entity that spreads across all Brokers
* Physically stored as one or more logs

## How it works
* producer sends message (binary payload) to kafka topic
  * broker adds to message: 
    * timestamp
    * referenceable identifier
* message gets appended to a time ordered sequential stream that belongs to the topic
* each message is a "fact" (immutable)
---
* consumer consumes message from kafka topic
  * **offset** indicates position in the topic's stream that consumer will start consuming from
  * offset is maintained by the consumer 
  * offset is established when consumer connects to broker 

## Topic Creation and Configuration - Partition Distribution
### Command to create a topic comes in to zookeeper
* Zookeper, which knows about what brokers/clusters are available, sees how many partitions and the replication factor specified during topic Creation
  * Zookeeper appoints leaders for each partition within the topic
    * Each leader will create a log for that partition.  
    * Each leader's partition will be independent of the partitions with other other leaders for that same topic
    * Each leader will be given metadata from the zookeeper about what other leader's have been assigned partitions
      * This is what allows any broker to redirect a producer to another broker 
    * Each leader sends health back 
* When a producer is ready to publish a message
  * It must know at least one broker in the cluster so it can find the leader of the topic's partition
  * When it connects to a broker, metadata about what brokers are avaialable for that topic is sent back 
* When a consumer is ready to consume messages
  * consumer connects to zookeeper to get back metadata about which brokers are avail for that topic, as well as, health status/availability of those brokers
  * consumer will retrieve messages based on each partition's offset
  * consumer will potentially retrieve messages out of order
  * consumer library is responsible for putting messages in order before providing the data back to the caller

## Notes
* kafka retains all published messages regardless of Consumption
* retetntion period is configuratble (default is 168 hours or 7 days)
* retention period is defined per topic
* physical storage of resources 