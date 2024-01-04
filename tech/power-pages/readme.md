# Power Pages

## Environments
* Power Pages Website can be developer, trial or production.  
* Power Pages environment can be developer, trial, sandbox, production 
* Every Power Page starts as a trial
  * A Trial Power Page **CANNOT** be directly converted to production if it was created in the Developer or Trial Environment
  * A Trial Power Page in a developer/trial environment **CAN** be migrated to a sandbox/production environment AND then converted to Production Power Page
* A Trial Power Page in a Developer or Trial Environment gets delted in 30 days or when the Developer or Trial environment expires, whichever is first
* A Trial Power Page in a Sandbox or Production Environment **SUSPENDED** in 90 days.  7 days after Suspension, it is deleted.
* An admin can convert a Trial or Suspended Power Page to Production Power Page.
  * To [convert to Production Power Page](https://learn.microsoft.com/en-us/power-pages/admin/convert-site#convert-a-website-from-trial-to-production), the Trial Power Page MUST be in a Sandbox or Production Environment 
* If the Power Page is deleted, the data for the site will NOT be deleted. 

## Dataverse
* All website configuration data is stored in Dataverse.
  * webpages
  * content snippets
  * site settings
  * user metadata
  * data store for business data
* Power Pages Users are NOT Dataverse Users and Dataverse RBAC do not apply to Power Pages Users.
* All users of Power Pages are stored in the Dataverse **contact** table
  * Data Access for these users is controlled through [web roles](https://learn.microsoft.com/en-us/power-pages/security/create-web-roles)
* Dataverse contain Configuration Tables and Data Tables
  * Configuration Tables are used to store configuration data for the Power Pages and cached for all users
  * Data Tables are used to store business data for the Power Pages and cached per user
    * Exceptions are anonymous users or tables with [global permission](https://learn.microsoft.com/en-us/power-pages/security/table-permissions#available-access-types)
    * Cache busting: 
      * record for a table is created, updated, or deleted by any user will clear the cache for the table for all Users.
      * 15 minutes if no changes are made
      * manually:
        *  if Preview is selected in design studio 
        *  utilize the clear config or clear cache option by navigating to the website with '/_services/about' appended to the URL of the website

## Connecting Power Pages to Dataverse
* Power Pages connect to Dataverse using Server to Server (S2S) connection. 
  * The connection is established via an Microsoft Entra application that is created when a Power Page is created. 
    * The naming convention for the Entra Application is `(Portals – {{portalid}})`
    * The id for the Entra Application can be found in the [workspace setup](https://learn.microsoft.com/en-us/power-pages/configure/setup-workspace) for that Power Page
    *  **DO NOT MODIFY THE ENTRA APPLICATION**
*  The connection uses the Dataverse **SYSTEM** or **APPLICATION** user.  [More Info](https://learn.microsoft.com/en-us/power-platform/admin/system-application-users).  Current sites use [Application user](https://learn.microsoft.com/en-us/power-platform/admin/manage-application-users).
   *  Can view Application User in Power Platfrom Admin Center -> selecting the environment -> and go to Acces -> Select S2S apps
      *  Application User format: `# Portals-<<site name>>`
      *  Application User Permissions: 
         *  Dataverse Security Roles: 
            *  Portal Application User
            *  Service Deleter
            *  Service Writer
         *  Column Security Profile
            *  System Administrator
         *  **DO NOT MODIFY SECURITY PROFILES**
*  When a Power Page is created: 
   *  The Entra Application is created
   *  Application Users are created
   *  An X509 certificate is generated and added to the Entra Application and App Server hosting the Power Page.    
      *  This cert allows access from application server to Dataverse
      *  **THE CERT EXPIRES EVERY TWO YEARS AND SHOULD BE [UPDATED](https://learn.microsoft.com/en-us/power-pages/admin/manage-auth-key)**

## Caching
* Power Pages cache data queried from Dataverse on the Application Server.
  * [Cached Data](https://learn.microsoft.com/en-us/power-pages/admin/clear-server-side-cache): 
    * Metadata/configuration tables represent all the tables 