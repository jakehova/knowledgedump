# Docker Commands

docker pull [<registry>/] <image name>: Pull an image down from Docker Hub
    * registry defaults to docker hub
    * microsoft registry: mcr.microsoft.com (docker pull mcr.microsoft.com/dotnet/core/sdk)

docker build -t <NAME OF IMAGE> <path to build from>: Build image
    * <Name of Image> => generally this is namespaced so could do something like: jakehova/node 
        * can add version number by using a colon at the end: docker build -t jakehova/node:1.0
    * <path to build from> => this could be just "." if youre running the build command from the directory that has the Dockerfile
    * Parameters: 
        * -f => specifies the docker file.  Defaults to "Dockerfile" so can leave this paramter off if thats the name of the file

docker exec <container id> <cmd to run>: allows you to run a command inside a running container
    * Example: docker exec d64323 node dbSeeder.js
        * This will execute "node dbSeeder.js" inside the running container with id d64323

docker network create <name of network>
    * Parameters:
        * -d <driver to use>  => specifies which driver to use for this network.  
            * Types of drivers: 
                * bridge => use if all containers will be on the same engine (HOST)
                * overlay => use if containers may be on different engines
                    * Requires access to key value store, cluster of hosts with connectivity to that key value store, properly configured engine daemon on each host in the cluster

docker run [OPTIONS] <image id>: Create a container from an image and run it. ORDER matters.  Cannot put OPTIONS after the image id
    * Parameters: 
        * -e <env key>=<env value> => pass in an environment variable
        * -p <port internal to docker container>:<port external that you access the internal port by> => define a port to run on
        * -d => run the container in the background (detached mode)
        * -v [<path on host machine>:][path used by code in container]=> creates a volume
            * Example: docker run -p 8080:3000 -v /var/www <image name>
                * in this case "/var/www" tells docker that this container will have a volume and that any code executed in the container can reference that path and have it write out to an actual location on the host machine.  The docker client will dynamically determine where that location on the host machine is
            * Example 2: docker run -p 8080:3000 -v ${pwd}:/var/www node
                * in this case "${pwd} specifies an actual location on the host machine of where to store these files (in this case pwd will return the current working directory)
        * -w "<docker internal directory>" >=> specify directory inside the container from which to run any command line arguments from
            * Example: docker run -p 8080:3000 -v ${pwd}:/var/www -w "/var/www" node npm start  
                * This runs the "npm start" command from the "/var/www" directory thats inside the running container
        * -it => make container interactive.  After running this, command line will be mapped to inside the container command line
            * "i" refers to interactive. "t" stands for tty
            * Example: docker run -it -p 8080:5000  -v ${pwd}:/app -w "/app" mcr.microsoft.com/dotnet/core/sdk /bin/bash
                * this creates a docker container from a dotnet core image.  the -it and "-w "/app" /bin/bash" basically says to run the "/bin/bash" command from the "/app" directory.  Since this is a Linux based container, that opens bash as the interactive shell setting the directory specified in the "-w" paramter.
        * --name <alias name of container> => apply a name to the container which allows for legacy linking
            * if this is left off then docker chooses a random name
            * Example: docker run -d -p 5000:5000 --name my-postgres
        * --link <container to link to>[:<alias for the container being linked to>] => create a connection between this container and another one
            * Example: docker run -d -p 5000:5000 --link my-postgres:postgres jakehova/node
                * links this new container with the my-postgres container.  Also creates the alias "postgres" that can be used within the container to link to the my-postgres container.

docker images: List Images

docker rmi <first few characters of image id>: Remove Image

docker ps: List Running Containers
    * Parameters    
        * -a => view all containers (not just the ones running)

docker start [containerid]: Start a Container

docker stop [containerid]: Stop a Container

docker rm [containerid]: Remove a Container
    * Parameters: 
        * -v => also remove volumes on host machine that are tied to this container

docker volume ls: list all volumes 
    * Parameters
        * -f: filter based on status (i.e. -f dangling=true)
        * -q: only display volume names
    * Associated Commands: 
        * docker volume prune: Remove all unused local volumes
        * docker volume rm <full volume name>


docker system|container|image|volume|network prune: Remove all unused docker objects

docker inspect <container id>: View Properties of a Running Container
    * Find the Running IP of a running container: docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container id>
    * Find the Volume location on the host machine: docker inspect --format '{{ .Mounts }}' <container id>

