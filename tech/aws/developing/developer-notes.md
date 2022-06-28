# Setting up containers and making them publicly accessible
**Note**: Note: This type of development certificate is not recommended for production use. It is used here for simplicity in a demo. For a production setup, you should use a certificate signed by a certificate authority. Recommendation: to run a production .NET application on ECS, use an AWS Application Load Balancer (ALB) to route traffic to a reverse proxy (Nginx) via an HTTPS listener configured to use a certificate signed by a certificate authority. The reverse proxy would then route traffic to the application. The reverse proxy and the application should also be configured to use TLS using valid certificates.

## Set up Container and Deploy to ECS/Fargate
* [Good Okta Writeup](https://developer.okta.com/blog/2022/01/19/deploy-dotnet-container-aws-fargate)
* Create a docker file (.net project)
```
#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["<Diretory Where csproj is now>.csproj", "<Directory where it will go in the container>"]
COPY ["Directory.Where.It.Is.Now.csproj", "Directory.Where.It.Will.Go/"]
RUN dotnet restore "Directory.Where.It.Will.Go/Directory.Where.It.Is.Now.csproj"
COPY . .
WORKDIR "/src/Directory.Where.It.Is.Nowr"
RUN dotnet build "Directory.Where.It.Is.Now.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Directory.Where.It.Is.Now.csproj" -c Release -o /app/publish
ARG CERT_PASSWORD
RUN dotnet dev-certs https -ep /app/aspnetapp.pfx -p ${CERT_PASSWORD}

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Directory.Where.It.Is.Now.dll"]
```
* Create self signed cert (certs/certs.md)
* Run container with https using self signed cert
```
# macOS/Linux
docker run -it --rm -p 5000:80 -p 5001:443 -e ASPNETCORE_URLS="https://+;http://+" -e ASPNETCORE_HTTPS_PORT=5001 -e ASPNETCORE_Kestrel__Certificates__Default__Password="mypass123" -e ASPNETCORE_Kestrel__Certificates__Default__Path=/https/aspnetapp.pfx -v ${HOME}/.aspnet/https:/https/ okta-chat

# Windows
docker run -it --rm -p 5000:80 -p 5001:443 -e ASPNETCORE_URLS="https://+;http://+" -e ASPNETCORE_HTTPS_PORT=5001 -e ASPNETCORE_Kestrel__Certificates__Default__Password="mypass123" -e ASPNETCORE_Kestrel__Certificates__Default__Path=/https/aspnetapp.pfx -v %USERPROFILE%\.aspnet\https:/https/ okta-chat
```
## Set up public access to Container
* Create ALB
    * Use the DNS associated with this ALB to route traffic to Container instances
    ```
    "loadBalancers": [
            {
                "containerName": "your-container-name-app",
                "containerPort": 80,
                "targetGroupArn": "arn:aws:elasticloadbalancing:eu-central-1:account-id:targetgroup/targetgroup-name/RANDOM-ID"
            }
        ],
    ```
* Create Target Group 
    ```
        aws elbv2 create-target-group \
        --name targetgroup-name \
        --protocol HTTP \
        --port 80 \
        --vpc-id vpc-YOUR_VPC_ID \
        --health-check-protocol HTTP \
        --health-check-path /healthcheck \
        --target-type ip
    ```
* Tie ALB path to Target 

## Set up ECR
* Log in to AWS/ECR and create repository
    * choose private
* go to the newly created repository and click on "view push commands".  Instructions will be similar to:
    * retrieve token using aws cli
    * build docker image.  remember to pass self signed cert created above
        * docker build --build-arg CERT_PASSWORD=mypass123 -t okta-chat .
    * tag the image
    * push the image to ECR

## Setup Fargate
* Log in to AWS/ECS
* Click Clusters -> Create Cluster -> Networking Only -> Next Step 
* Name the Cluster
* Click Task Definitions -> Create new Task Definition -> Select Fargate as startup type -> Next Step
* Name the task Definition
    * mem .5 GB / Task CPU .25 vCPU is a good size for basic functionality
* Click Add Container (name the container same as th etask definition)
* Set Image to the ECR image path created in previous step
* Set soft limit to 512 and add port 80/443
* Set Env variables
```
ASPNETCORE_URLS="https://+;http://+"
ASPNETCORE_HTTPS_PORT=443
ASPNETCORE_Kestrel__Certificates__Default__Password="mypass123"
ASPNETCORE_Kestrel__Certificates__Default__Path=./aspnetapp.pfx
```
* Click Create
* Go back to cluster, click on tasks tab, click "Run new task"
* **Note:** Here’s a recommendation: Create services instead of tasks for production to take full advantage of the elastic scaling capabilities of ECS. I’m using tasks directly for the simplicity of the demo. When using an ALB (application load balancer) to route traffic to the application, use of services is also required.
* Select Fargate as Launch type
* Select default VPC and Subnets under VCP and Security Groups
* Click "Edit" next to Security Groups -> Add Rule: allow inbound on 443 (HTTPS, TCP, 443, Anywhere)
* Click "Run Task"
* Go back to cluster and click on the task id that was created, copy the public ip 


