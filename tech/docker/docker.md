# Docker

## What
Simplifies building, shipping, and running apps in different environments.
Runs on a Docker Client.
Docker Client is native to Linux (Linux Container Support LXC) and Windows Servers  (Windows Server Container Support)

## Layered File system
- Layer 1 - A container has interface access to the read only files contained in the image.  A container also has a thin read/write layer.
- Layer 0 - An image contains a bunch of read only files

- The benefit of this is that you can use one image and have multiple containers on top of that one image.  Since that image is read only, each container built on top of it can be sure that its working from a consistent foundation


## Terms
Image - Contains instructions for how to create an active container. Is a read only template composed of layered filesystems to share common files and create Containers
Container - Created from an Image and is what actually runs your application.  An isolated and secured shipping container created from an image that can be run, started, stopped, moved, and deleted.
Volumes - special directory reference in a container.  The aliased directory (the actual storage location that the reference points to) can be shared and reused among containers by pointing those individual containers directory references to that same storage location on the host machine.  
    * A volume path is specified in a container.  That path is an ALIAS for an actual directory on the HOST machine.  
    * Updating an image does not affect a volume.  
    * Volumes are persisted even after a container is deleted.

## Links
[Common Commands](./developing/docker-commands.md)
[Developer Info](./developing/docker-for-developers.md)
