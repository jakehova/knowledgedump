# Pulumi

**Commands**
* pulumi new typescript - creates new pulumi typescript project
* pulumi up - cretes resources
* pulumi stack - lets you see the current stack resources
* pulumi plugin ls - lists the plugins and their versions
* pulumi destroy - removes resources in current stack
* pulumi stack output <exported output variable name> - returns the value of that outputted value from the current stack
* pulumi logs - retrieves cloud trail logs that are generated against stack (so for an api gateway will give history of requests)
* pulumi config set <key> <value> - sets configuration variable for pulumi environment
    * ex: pulumi config set aws:region us-west-2

**C# Commands**
* pulumi new csharp -> creates a new pulumi c# project
* dotnet add package Pulumi.Aws -> Adds the Pulumi AWS nuget package to the project

**Environment**
* [file] Pulumi.dev.yaml - contains environment specific configuration variables
    * This gets updated or created when you run: pulumi config
* If you have multiple aws profiles setup you can:
    * 1) Set AWS_PROFILE as an environment variables: $env:AWS_PROFILE = "<profile name>"
    * 2) Set Pulumi configuration to that profile: pulumi config set aws:profile <profile name>

**Notes**
* curl $(pulumi stack output <exported output variable name that contains url>) - checks the url