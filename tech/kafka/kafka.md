# Kafka
## What is it? 
* Kafka is a distributed data Store
* Optimized for injesting and processing LARGE amounts of data in real time
* Event Streaming Platform
* Scalable & Fault Tolerant
* Implements BOTH queuing and pub/sub messaging models 
* All data is stored as key value byte arrays
* Process
    * Producer (any app or service) sends data 
    * Kafka enqueues the data in a Log (a log is essentially an ordered queue)
        * Each Log has one or more Segment(s)
        * A segment is created for each subscriber to a log

* Kafka Server: 
    * Kafka Brokers (servers that manage writing/reading from logs)
    * Kafka APIs: 
        * Producer API - gets data into Kafka.  publishes data to a Kafka Topic
        * Consumer API - gets data out of Kafka. subscribes to topic(s) and gets sent data as it arrives at a topic
            * Request asks for a topic and an offset (offset says which record in the log do you want to return data from)
        * Streams API - used to receive data from a topic, transform it in some way, and output it to a different topic.  For example, if you subscribe to the "login_attempt" topic, you could take that login attempt, supplement it with an application name and then push the new message to a different topic that some other applications are subscribed to via consumer api.   
        * Connector API - allows you to add applications or data systems to push/pull data to/from kafka

```mermaid
    graph TD;
        Producer_API-->Kafka_Broker
        Kafka_Broker-->Consumer_API
        Connector_Input_via_API-->Kafka_Broker
        Kafka_Broker-->Connector_Output_via_API
        Kafka_Broker<-->Streaming_Engine
```

## Core components
* Brokers - Storage nodes
* Log - Write only and immutable list of records
    * Size can be configured based on size or time (7 day default retention time for each topic)
* Topics - a logical grouping of events 
    * Events are stored in a log on the broker in a directory named after the topic
    * A topic can be anything.  You create topics based on how you want to add specificity to data being passed in.  For example, if you are using Kafka to monitor login activity.  You could create a topic for "login_attempt" where every login attempt would be grouped. 
* [Serdes](https://kafka.apache.org/30/javadoc/org/apache/kafka/common/serialization/Serdes.html) - Types that are defined and used inside Kafka
    * Name comes from: **SER**ialize and **DES**erialize
    * Can also use [Avro](https://avro.apache.org/docs/current/) to serialize/deserizalize complex Types
    ```
    final Map<string,string>serdeConfig = Collections.singletonMap(AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, SCHEMA_REGISTRY_URL);

    final SpecificAvroSerde<WidgetType> widgetSerde = new SpecificAvroSerde<>();

    widgetSerde.configure(serdeConfig, false);
    ```
* Stream - unbounded sequence of structured data (commonly referred to as events)
* kStream - JAVA library abstraction over a stream.  representation of data where each piece of data is treated in isolation (immutable objects)
    * Does NOT live on the broker
    * Connects to a broker over the network via host:port
    ```
    final KStreamBuilder builder = new KStreamBuilder();
    
    final KStream<String, Widget> widgetEvents = builder.stream(Serdes.String(), widgetSerde, "widget-events");
    ```
* kTable - JAVA library abstraction over a stream where latest data is the data that is used (mutable objects).  
    * each kTable can subscribe to only one topic at a time
    * a kTable only focuses on one partition of it's topic at a time
    * backed by a state store (seems like a dictionary with the key of each record that comes in being the key of the state store dictionary)
    * uses "commit interval" or cahce size to determine when to push events.  Setting it to 0 would forward every event
    * kStreams forward EVERY event.  kTables only forward events when "commit interval" expires OR when cache size is exceeded.
* global kTable - same as kTable but stores ALL records across ALL partitions
    * used for smaller datasets that dont change much (i.e zip codes/country codes/etc)

## JOINS
* allows you to join two streams/tables together to create a single kStream or kTable
* requires keys to be the same type
* can use the same value type or create a new value type
* Types of join: 
    * Inner - will only emit a record if  if both sides have the key within the defined window 
    * Outer - will always emit an event if either side of the stream has an event
    * Left-Outer - will emit an event only if the left stream produces a record
* Objects that can join:
    * stream-stream: joins two streams when a key in the left stream and a key in the right stream appear within a specified interval of time (called a windowed join due to the join only occurring in that window of time)
        * uses a local state store during this interval of time 
        * can do inner, outer, left-outer joins
    * stream-table: joins a stream with a table 
        * can join a regular kTable or a global kTable
        * can do inner, left-outer (can only use if kStream is on left side)
    * table-table: joins two tables
        * can do inner, outer, left-outer

## Example Usage
* A systems acts as a producer and sends a **Record** to a Kafka Broker
* **Record** is examined and written to a log/segment that corresponds with one or more topics
* The **Record** is published to a topic endpoint and available for Consumption
* Consumption occurs by any number of consumers.  Consumers are created via:
    * Consumption API
    * kStream
    * kTable
    * join 
    
```mermaid
    flowchart LR
    Producer-->Broker
    subgraph kafka
    Broker-->Log
    Log-->Topic1
    Topic2
    end
    Topic1-->Consumer
    subgraph kStream
    Topic1-->JavaApp
    JavaApp-->Topic2
    end
    subgraph join
    Topic1-->JoinApp
    Topic2-->JoinApp
    end
```

## Sample Code
### JOIN 
```
KStream<string,string> leftStream = builder.stream("topicA");
KStream<string,string> rightStream = builder.stream("topicB");

ValueJoiner<string, string, string> valueJoiner = (leftValue, rightValue) -> {
    return leftValue + rightValue;
}

leftStream.join(rightStream, valueJoiner, JoinWindows.of(Duration.ofSeconds(10)));
```

### kTable
```
final StreamsBuilder builder = new StreamsBuilder();
KTable<string,string> myKTable = builder.table("<topic name>", Materialized.with(<type of key>, <type of value>))
```

```
final StreamsBuilder builder = new StreamsBuilder();
KTable<string,string> myKTable = builder.table("widgets", 
                                    Materialized.with(Serdes.String(), Serdes<Widget>))
```

### kStreams
```
// format for reading from one topic and pushing to another topic
builder.stream("<topic name>", Consumed.with(<type of key>, <type of value>))
       .filter((key, value) -> value.<property accessor>.equals("somevalue"))
       .to("<other topic name>", Produced.with(<type of key>, <type of value>))
```

```
// consume "widgets" topic
// get just the ones that are red property for color
// publish those to a new topic called "widgets-red"
final StreamsBuilder builder = new StreamsBuilder();
KStream<String, Widget> widgetStream = 
builder.stream("widgets", Consumed.with(stringSerde, widgetsSerde))
       .filter((key, value) -> value.getColor.equals("red"))
       .to("red-widgets", Produced.with(stringSerde, widgetsSerde))
```

There are a variety of functions you can take on a stream to transform it (map, mapvalues, filter, peek, etc)

## Testing
* Use [TopologyTestDriver](https://www.confluent.io/blog/test-kafka-streams-with-topologytestdriver/) 
* Use [MockSchemaRegistry](https://medium.com/bakdata/transparent-schema-registry-for-kafka-streams-6b43a3e7a15c)
