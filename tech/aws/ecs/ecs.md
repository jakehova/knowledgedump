# ECS (Elastic Container Service)

## Background
* [AWS Source Info](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

## Terms
* Task Definition — This a blueprint that describes how a docker container should launch. If you are already familiar with AWS, it is like a LaunchConfig except instead it is for a docker container instead of a instance. It contains settings like exposed port, docker image, cpu shares, memory requirement, command to run and environmental variables.
* Task — This is a running container with the settings defined in the Task Definition. It can be thought of as an “instance” of a Task Definition.
* Service — Defines long running tasks of the same Task Definition. This can be 1 running container or multiple running containers all using the same Task Definition.
* Cluster — A logic group of EC2 instances. When an instance launches the ecs-agent software on the server registers the instance to an ECS Cluster. This is easily configurable by setting the ECS_CLUSTER variable in /etc/ecs/ecs.config described here.
* Container Instance — This is just an EC2 instance that is part of an ECS Cluster and has docker and the ecs-agent running on it.

## Creating
1. Create Security Group for ECS instance to operate in
2. 