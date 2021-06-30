# Pulumi

**Architecture**
* Project is any folder that contains a "Pulumi.yaml" file
  * Programmatically access: let project = pulumi.getProject();
* A Stack is an isolated instance of a pulumi program
  * Each stack has a Pulumi.<stack name>.yaml file 
    * this file should be in the root directory of the project
  * Stacks are generally used to denote different phases of development (dev, staging, prod, etc)
  * Create new: pulumi stack init [<org name>/][<project name>/]<stack name>
* Deploy a project 

**Commands**
* pulumi new typescript - creates new pulumi typescript project
* pulumi up - cretes resources
* pulumi stack - lets you see the current stack resources
* pulumi plugin ls - lists the plugins and their versions
* pulumi destroy - removes resources in current stack
* pulumi stack output <exported output variable name> - returns the value of that outputted value from the current stack
  * Create an ouput variable by adding:     
    * Add Property: public Output<string> PropertyName {get;set;}
    * Add Output decorator to property: [Output]
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
    * Use the profile
      * 1) Set AWS_PROFILE as an environment variables: $env:AWS_PROFILE = "<profile name>"
      * 2) Set Pulumi configuration to that profile: pulumi config set aws:profile <profile name>
    * Set $env variables: 
      * $env:AWS_ACCESS_KEY_ID="<value>"
      * $env:AWS_SECRET_ACCESS_KEY="<value>"

**Notes**
* curl $(pulumi stack output <exported output variable name that contains url>) - checks the url
* 