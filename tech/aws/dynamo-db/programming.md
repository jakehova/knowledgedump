# .NET and Dynamo DB

## Helpful Links
* [.NET SDK Docs](https://aws.amazon.com/sdk-for-net/)
* [.NET SDK Dynamo Docs](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/dynamodb-intro.html)

## Setup
* Prerequisite
    * [Install Java](https://java.com/en/download/manual.jsp)
    * [Install AWS CLI](https://aws.amazon.com/cli/)
* [Setup Locally](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)
* [Download Local Version of Dynamo](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
    * Unzip files into a local directory
    * Navigate tot he **DynamoDBLocal.jar** file in the unzipped directory and run the command: java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb
        * DynamoDB  uses port 8000 by default
    * Alternatively, install via Docker: 
```
// docker-compose.yml
version: '3.8'
services:
  dynamodb-local:
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    image: "amazon/dynamodb-local:latest"
    container_name: dynamodb-local
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal
```
OR, use the following if you want app and dynamo to run in different containers
```
version: '3.8'
services:
  dynamodb-local:
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    image: "amazon/dynamodb-local:latest"
    container_name: dynamodb-local
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal
  app-node:
    depends_on:
      - dynamodb-local
    image: banst/awscli
    container_name: app-node
    ports:
     - "8080:8080"
    environment:
      AWS_ACCESS_KEY_ID: 'DUMMYIDEXAMPLE'
      AWS_SECRET_ACCESS_KEY: 'DUMMYEXAMPLEKEY'
    command:
      dynamodb describe-limits --endpoint-url http://dynamodb-local:8000 --region us-west-2
```
* Verify that dynamo is up using AWS CLI: aws dynamodb list-tables --endpoint-url http://localhost:8000
