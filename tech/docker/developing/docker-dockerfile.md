# Dockerfile 

## What
* Text file describing how to create the image
* Primary Commands: 
    * "FROM" which specifies which image to build this image from
    * "LABEL" specifies who the author is
    * "RUN" specifies how its run (like npm install)
    * "COPY" copies code into the container
    * "ENTRYPOINT* set the main entry point via JSON array 
    * "WORKDIR" set the working directory (like which folder cotnains the package.json)
    * "EXPOSE" default port that the container runs with
    * "ENV" define environment variables
    * "VOLUME" define volume and control how its handled/stored by the HOST system

## Creating a Custom Dockerfile


## Building an image
    * docker build -t <tag name> <path to dockerfile context>
        * tagname should be namespaced. example: docker build -t jakehova/v1/node 

## Example

```
FROM node
LABEL author="Jacob"
COPY . /var/www         // copy the files that are in the current working directory (relative to where you run the build command) to the container in a directory named "/var/www"
WORKDIR /var/www        // any commands run during the docker run command would be default run in this folder location inside the container
RUN npm install
EXPOSE 8080
ENTRYPOINT ["node", "server.js"]
```

```
FROM node:latest
LABEL author="Jacob Cheriathundam"
ENV NODE_ENV=production
ENV PORT=3000
COPY . /var/www
WORKDIR /var/www
VOLUME ["/var/www"]
RUN npm install
EXPOSE $PORT
ENTRYPOINT ["npm", "start"]
```

**Development DotNet Core docker**
```
FROM mcr.microsoft.com/dotnet/core/sdk

LABEL author="JAcob"

ENV ASPNETCORE_URLS=http://*:5000
ENV DOTNET_USE_POLLING_FILE_WATCHER=1
ENV ASPNETCORE_ENVIRONMENT=development

WORKDIR /app

ENTRYPOINT ["/bin/bash", "-c", "dotnet restore && dotnet watch run"]
```

**Production Dotnet Core docker**
```
FROM mcr.microsoft.com/dotnet/core/aspnet AS base           // alias the foundational image of the production aspnet image as "base"
WORKDIR /app                                                // set the working directory where commands will be run to "/app"

FROM mcr.microsoft.com/dotnet/core/sdk AS build             // alias the foundational image of the dotnet core sdk as "build"
WORKDIR /src                                                // set the working directory in the container to to "/src"
COPY ["dotnet-mvc.csproj", "./"]                            // copy the csproj file from the directory that has the dockerfile to the "/src" directory in the container
RUN dotnet restore "./dotnet-mvc.csproj"                    // run the dotnet restore command for the csproj
COPY . .                                                    // copy all the code from the directory that has the dockerfile to the "/src" directory
WORKDIR "/src/."                                            // set the working directory to inside the "/src" directory
RUN dotnet build "dotnet-mvc.csproj" -c Release -o /app     // run the build and set compile mode to Release and output the result to the "/app" dir

FROM build as publish                                       // alias the foundational image produced in the above block of code as "publish"
RUN dotnet publish "dotnet-mvc.csproj" -c Release -o /app   // run the publish command with compile set to Release mode and output going to the "/app" dir

FROM base as final                                          // alias the production .net run time as "final"
ENV ASPNETCORE_URLS="http://*:5000"                         // create an environment variable
EXPOSE 5000                                                 // expose port 5000
WORKDIR /app                                                // change the working directory to "/app" which is where all the publish output artifacts are
COPY --from=publish /app .                                  // copy all the code in the "/app" dir from the publish image generated above to the WORKDIR (same)
ENTRYPOINT [ "dotnet", "dotnet-mvc.dll" ]                   // run the "dotnet dotnet-mvc.dll" command
```