# IAM - Identity Access Management

**Secure the Root Account**
- root account - email address used to sign up for AWS.  This account has FULL Administrative Access.
- process to secure: 
    - click username -> my security credentials page
    - turn on MFA

**Controlling User's Actions**
- IAM runs at a global level (not region)
- Controlled via Policy Documents 

**Policy Documents**
- Policy Documents (JSON) are JSON files that are assigned to Groups, Users, and/or Roles to control access to AWS
``` 
// Administrator Policy Document
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```
- Explicit Deny in an Effect overrides any Allow for that same resources.


**Building blocks of IAM**
- Users should be a single physical person that is added to Groups which are created by function.
- Roles are used for internal AWS functions (service to service communications primarily)
- **Best Practice** - Users should inherit their permissions from groups
- **Best Practice** - Try not to assign permissions to individual users
- **Best Practice** - Only assign the MINIMUM amount of privileges they need to do their job.