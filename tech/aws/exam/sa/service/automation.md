# Automation

* Use cloud formation to build infrastructure and deploy the app layer with OpsWorks Stacks
* **Cloud Formation** Templates
    * Can write in JSON/YAML
    * Create Template -> Submit it to cloud formation engine -> Generates architechture stack (a group of resources that can be managed together (like a VPC, Subnet, Security Group, EC2 instances all creating an environment would be 1 stack))
* **Systems Manager** - Set of capabilities to enable automated configuration and ongoing mgmt of systems at scale
    * Run Command - lets you run a console against all instances
    * Patch mgmt
    * Session Mgr 
    * Maintenance Windows
    * State Mgr
    * Inventory
* **AWS OpsWorks** - configuration managment services specifically:
    * Options
        * Stacks - provides a simple and flexible way managing stacks and applications (deploy and monitor apps in your stack)
        * Chef - 
        * Puppet
    * Setup
    * Configure
    * Deploy
    * Undeploy
    * Shutdown
* **AWS Elastic Beanstalk** - provisions and operates the infrastructure and manages the application stack for you
    * Completely transparent you can see everything created
    * You provide the code and EB handles creating http server, app server, language interpreter, OS, Host
    * Provides you a unique domian name for your app environment
