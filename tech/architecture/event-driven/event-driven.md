Domain Event (orange) - an action that is taken to trigger a business process
Policy (purple) - process that is kicked off by a domain even (naming always starts off witth "whenever")
External System (pink) - any external system (i.e. paypal)
Command (blue)- actions that occur because of a user or scheduler 

DDD
- Define Aggregate - Label every action that happens in the system (Scheduled Order, Scheduled Delivery, etc)
- Define Bounded Context - Put each label into the domain that it exists in ("Scheduled" in Order Domain, "Scheduled" in Delivery domain)

Example Process Flow for a Checkout Process
- Define Aggregate:
    - Start with initial domain events: Items Added to Basket, Address Submitted, Payment Details Submitted
    - Drill down basic events to account for outcomes (more domain events): Basket Updated or Alert Set (if basket update failed), Address Validated, Address Rejected, Payment Approved, Payment Declined
    - Add in Policy to tie domain events to outcomes: Items Added To Basket ties to "In Stock" Policy which triggers the outcome for Items Added (Basket Updated or Alert Set).  Same for the other domain events
    - Add Commands that occur that trigger the domain events: User adds item to basket triggers Items Added To Basket domain event, User types in their address triggers Address Submitted, User adds their payment details triggers Payment Details Submitted
- Define Bounded Context
    - Group the Aggregates into the process category they belong to: 
        - Order Bounded Context => Contains Items Added to Basket and Address Submitted
        - Payment Bounded Context => Contains Payment Details Submitted 
        - Shipping Bounded Context => <nothing yet but this is the basic idea>


KAFKA
- Distributed Streaming Platform Written in Java and run in JVM
- High throughput (No serialization/deserialization)
- All data going to and coming from Kafka is binary 
    - Can be configured to use Zero Copy (ONLY FOR NON-TLS CONNECTIONS)
        - Zero Copy takes binary data from the network card and writes it directly to the hard disk
        - What happens if Zero Copy is not used, is binary data is written to JVM Heap and JVM writes data from Heap to Hard Drive
- Components
    - Broker 
        - dedicated server with dedicated hardware
        - Handles message coming in (writes the message to hard disk) and going out
        - In a cluster, Broker will immediately pass message to other brokers in teh cluster for backup and load balancing purposes
    - Zookeeper
        - handles managing all brokers
        - centralized service that all brokers are tied to
- Record (Message)
    - Contains Key: any, Value: any, Timestamp 
- Topic: 
    - Each topic is managed by the zookeeper
    - Each topic can have a Max Size associated with it
    - Records are stored in the broker according to their topic
    - Types 
        - Delete - 
            - record gets added to delete topic based on retention time or topic size
        - Compact
            - upsert messages based on key value of record
- Distribution
    - Kafka uses partitions.  same topic is split in multiple partitions and each partition lives on a different broker.  
        - if there are more partitions than brokers, then multiple partitions will exist on same broker
        - **Note** Records are not replicated across partitions UNLESS the same record has been generated multiple times.
    - Default strategy for assigning a record to a partition is "even", so evenly distribute records across partitions
    - Can create replicated partitions => duplicates of partition on a different broker.  
        - Copies are immediately crated on replciated partition after write to initial broker is commute
- Producer
    - App that creates "Producer Record"  to send to Kafka
        - Producer record is a special record where the key is specific to an entity type in the application (like user id)
        - composed of key/value.  
        - App has a Key Serializer and Value Serializer to convert the key/value into binary before sending to Kafka
        
