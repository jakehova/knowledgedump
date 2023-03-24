# Installation

* Save [docker compose](docker-compose.yml) file
* Run 
```
docker compose up -d
```

## Interacting with Docker Container
* Create topic: 
```
docker exec broker kafka-topics --bootstrap-server broker:9092  --create --topic quickstart
```

* Use **kafka-console-producer** tool to write messages to the topic
    * Setup producer for writing to topic:
    ```
    docker exec --interactive --tty broker  kafka-console-producer --bootstrap-server broker:9092 --topic quickstart
    ```
    * From terminal window, the tool is now waiting for you to send messages to the topic.  Press ctrl+c to exit

* Use **kafka-console-consumer** to read messages from the topic
    * Setup consumer for reading from topic: 
    ```
    docker exec --interactive --tty broker kafka-console-consumer --bootstrap-server broker:9092 --topic quickstart --from-beginning
    ```
    * Enter some messages in the "producer" tool terminal and see them come through on the consumer terminal

* Shut down Container
```
docker compose down
```
