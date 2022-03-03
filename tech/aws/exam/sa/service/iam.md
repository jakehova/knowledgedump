# IAM

* Root User has unlimited access to your AWS account.  Cannot be limited. NEVER USE ROOT USER
* Identity Based Policy
    * Attached to: User, group, or role
* IAM Groups
* IAM Roles - A role lets you define a set of permissions to access the resources that a user or service needs
    * Use Cases: 
        * AWS Resources with access to AWS services
        * Provide access to externally authenticated users
        * Provide access to third parties 
        * Can be used to grant credentials temporarily 
* Using Groups vs Using Roles
    * Roles are for individual things (users or services).  Groups are for users.  Your employees/contractors would be part of groups.  If one of them needs access to a service or environment temporarily, then you would create a role and assign that role to them. 
* STS Identity Broker
* SAML 
* **AWS Cognito** - fully managed service that provides authentication, authorization, and user management for web/mobile apps
    * User Pools - user directory 
    * Identity Pools - federated identities - create uniqe identies for your users and federate them with your users
* **AWS Landing Zone** - helps customers more quickly set up a secuire, multi-account AWS environment based on AWS best practices
* **AWS Organizations** - Centralized account management
    * NO CHARGE & BEST PRACTICE To manage users 
    * Group-based account management
    * Policy-based access to AWS Services
    * Automated account creation and management
    * Consolidated billing
    * API-based
    * Root has OUs. OU has AWS Account * Resources. Service Control Policies apply to each layer.