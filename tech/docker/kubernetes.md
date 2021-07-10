# Kubernetes

## What
Container and Cluster management
Supported by all major cloud platforms
Provides a declarative way to define a cluster's state using manifest files (YAML)
Interact with Kubernetes using kubectl

Has load balancing
orchestrate storage
automate rollouts and rollbacks
mange workloads
self healing containers
manage secrest and configurations
horizontal scaling 

## Commands
* kubectl version =>  get the version 
* kubectl get [deployments | services | pods] => list out the respective item
* kubectl run <container name> --image=<image name> =>  run a specific image
* kubectl apply -f [<fileName> | <folderName>] => run all the compose files in a folder or file
* kubectl port-forward [<name of pod>] <port number to expose>:<port number inside container to be forwarded> => take a pod and open it up to an external port
* kubectl delete deployment <name of deployment> => remove deployment

## High Level Overview
A Master node has worker nodes.
A Worker node has one or more pods
A Pod has one or more containers

A group of nodes controlled by a master node is called a Cluster

## Installing
* [Minikube](https://github.com/kubernetes/minikube)
* Comes with Docker Desktop

## Converting from Docker Compose to Kubernetes
* [Compose on Kubernetes](https://github.com/docker/compose-on-kubernetes)
    * docker stack deploy --orchtestrator=kubernetes -c docker-compose.yml <name of stack>
* [Kompose](http://kompose.io)
    * transltes and converts docker compose files into files required for kubernetes
    * [Install](https://kompose.io/installation/) it on your machine
    * run "kompose convert" in the same directory as the docker-compose.yml file

## Running containers in Kubernetes




