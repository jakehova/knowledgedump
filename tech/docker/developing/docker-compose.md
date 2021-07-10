# Docker Compose

## What 
Manages the app lifecycle (Start, stop, rebuilding containers)
View status of running containers
Stream the log out put of runnings containers
Run a one-off command on a containers

## docker-compose.yml 
**node app connected to a mongo db**
```
version: "3.x"
services: 
    node:                       // name of the container
        build: 
            context: .          // essentially WORKDIR
            dockerfile: node.dockerfile //dockerfile to use
        ports: 
            - "3000:3000"
        networks: 
            - nodeapp-network   //bridge network to join
    mongodb:
        image: mongo            // image to build from
        networks: 
            - nodeapp-network
networks: 
    nodeapp-network:
        driver: bridge
```
**.net core app connected to postgres db**
```
version: '2'
services: 
    web: 
        build: 
            context: .
            dockerfile: aspnetcore.dockerfile
        ports: 
            - "5000:5000"
        networks: 
            - aspnetcoreapp-network
    postgres:
        image: postgres
        environment: 
            POSTGRES_PASSWORD: password
        networks: 
            - aspnetcoreapp-network
networks: 
    aspnetcoreapp-network:
        driver: bridge
```
## Commands
* docker-compose build [<image id>]=> builds the images using the information in docker-compose.yml file
* docker-compose up => create and start the containers that were created
    * run detached: -d
* docker-compose down => stops and removes all the containers
    * remove all images: --rmi all 
    * remove all volumes: --volumes
* docker-compose logs => 
* docker-compose ps => view all containers
* docker-compose stop/start 
* docker-compose rm => remove all the containers created

