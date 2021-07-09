# Docker Commands

DOCKER:
Build image
docker build -t "<NAME OF IMAGE>:Dockerfile" .

Run Image
docker container run -d 

Start a Container
docker container start [containerid]

Stop a Container
docker container stop [containerid]

Remove a Container
docker container rm [containerid]

Remove all unused docker objects
docker system|container|image|volume|network prune

​​​​​​​​​​​​​​​​​​​​​​​​​​​​docker run -it algorand/testnet
./goal node start -d data

vmmem/wsl eating up resources
 - shut down wsl: wsl --shutdown