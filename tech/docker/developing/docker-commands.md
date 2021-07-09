# Docker Commands

docker pull <image name>: Pull an image down from Docker Hub

docker build -t "<NAME OF IMAGE>:Dockerfile" .: Build image

docker container run: Run Image: 
    * Parameters: 
        * -p <port internal to docker container>:<port external that you access the internal port by> => define a port to run on
        * -d => run the container in the background (detached mode)

docker images: List Images

docker rmi <first few characters of image id>: Remove Image

docker ps: List Running Containers
    * Parameters    
        * -a => view all containers (not just the ones running)

docker start [containerid]: Start a Container

docker stop [containerid]: Stop a Container

docker rm [containerid]: Remove a Container

docker system|container|image|volume|network prune: Remove all unused docker objects

docker inspect <container id>: View Properties of a Running Container
    * Find the Running IP of a running container: docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container id>