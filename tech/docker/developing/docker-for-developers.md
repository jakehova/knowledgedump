# Docker For developers

## How to create a container volume that points to source code 
    * have the code running locally properly.  
    * from the command line, migrate to that directory
    * pull a docker container capable of hosting that code
    * during the "docker run" command:
        * specify the volume mapping that has the current working directory (referred to ${pwd}) mapped to the directory in the container where the code is stored.
        * specify the working directory with the 'w' command as the mapped directory
        * "run the code" by using a command line parameter at the end of the docker run command
            * example: "npm run start" or "dotnet watch run" at the end of the command

## Communication between Containers
    * Legacy Linking
        * Run container with a name
            * Example: docker run --name my-postgres jakehova/db
        * Link to a running container by name
            * Example: docker run --link my-postgres:postgres jakehova/node
                * Example uses an alias of "postgres" that the node app can use to refer to the postgres container
    * Bridge Network
        * Create custom bridge network and give it a name
            * Example: docker network create -d bridge isolated_network
        * When running container, assign it to a network 
            * A container can belong to multiple networks
            * Example: docker run --net=isolated_network --name=mongodb mongo
        