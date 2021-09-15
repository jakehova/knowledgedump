# SNS/SQS

* Problem: Web Tier and App Tier are tightly coupled.
    * Solution 1: Put Elastic Load Balancer (ELB) in between web and app tier.  Issue with this is that if there are any network issues, use queueing
    * Solution 2: Use SQS 
**SQS**
* Pros
    * Fully managed queuing service
    * Messages are stored until they are processed and deleted
    * Acts as a buffer between senders and receivers
* Types
    * Standard Queue: At least once delivery
        * Messaging Limit: Nearly unlimited
    * FIFO Queues: Messages are processed exactly once in the exact order
        * Messaging Limit: 300 Messages a second 
* Features
    * Persists Messages
    * Long Polling
    * Send/receivers
    * One to One
    * Dead Letter Queue (DLQ): Move messages that cant be processed to this queue.
    * Visibility Timeout: When a message is pulled off the queue while its not deleted it is made invisible to other processes acting on the queue
    * Long Polling: Reduces costs 
* Message has limitation of 256k
* Process
    1 Producer sends message to queue which gets distributed redundantly
    2 Message gets picked up for processing by consumer and visibility timeout starts
    3 Message gets deleted by consumer after receiving and processing it
**SNS**
* Coordinates and manages messaging between publishers and subscribers
* Subscription Types
    * Email
    * Http/Https
    * SMS
    * SQS
    * Lambda Functions
* Characteristics
    * No message persistence
    * Push 
    * pub/subscribers
    * one to many communication
    * Single Published Message
    * No recall options
    * Http/Https retry
    * Order and delivery not guaranteed
**Amazon MQ**
* When to Use: Using a messaging system with an existing application and want to move the application to the cloud otherwise use SNS/SQS
* Manged message broker service for Apache MQ
* Makes it easy to setup and operate message brokers in the cloud
* Direct access to Active MQ conole
* Compatible with open standard APIs and protocols: JMS, NMS, AMQP, STOMP, MQTT, and WebSocket