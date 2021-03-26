# IAM

* Create specific policies for the CloudFormation permissions you want to grant to a specific user/groups.
    * Ex: Create a policy for users you only want to be able to view a stack 
    * Ex: Create a policy for users to credate, update, delete stacks
    * Anatomy of a policy: 
        * Version - Version of the policy language. Use the latest version "2012-10-17"
        * Statement - Container for the following elements
            * SID (o) - Optional ID to differentiate between statements
            * Effect - Allow or Deny access
            * Principal - Indicate the account, user, role or federated user to which you would like to allow or deny access.
            * Action - List of actions that the policy allows or denies
            * Resource - List resources to which the actions apply
            * Condition (o) - Specify which circumstances under which the policy grants permission
* Users who can create/delete stacks, must also have appropriate permissions to the resources in the stack 