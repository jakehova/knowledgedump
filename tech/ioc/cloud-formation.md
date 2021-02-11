# Cloud Formation

**Best Practices**
    * Dont change infrastrcuture directly that was created by cloud formation (will lead to drift and template becomes invalid)


**Cloud Formation Template:**
    * Can use to describe the infrastructure using cloud formation template written with: 
      * JSON
      * YAML ([[yaml]])
    * Upload template to S3 bucket so that Cloud Formation can create stack from it
    * Cloud Formation Template is a class.  An instance of a template is a stack
      * Stack exists inside cloud formation
    * How to create stack from template: 
      * Create Template
      * Go to cloud formation -> stacks -> create stack
      * Point to template either with the s3 url or template file
      * Configure parameters (0.0.0.0/0 is allow all traffic)
      * Add tags
      * Need to create a policy and attach it to a role and use it to associate with the created elements in the stack
      * fill out advanced options
      * Create stack

