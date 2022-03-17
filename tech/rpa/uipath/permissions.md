# Permissions

# What
There are canned roles and custom roles you can provide to users.  Dont apply custom permissions to individual users.  Create roles and assign those roles to people so that its easier to maintain
* Administrators - org level role 
    * Can perform all administrative actions at an org level
        * creating/updating tenants
        * managing users
        * viewing audit logs
* Everyone - org level low level user 
* Automated users
    * Automation user at folder level 1
    * Allow to be Automation user at tenant level
* Automation Developers

# Roles
As a general guide, an RPA team would consist of these roles: 
* RPA Developer - This is the person working in Studio/StudioX/StudioPRO
* Solution Architect - Designs the technical architecture of the RPA solution (what apps will be used, what types of automations will be used,  which robot to use for each automation  (attended/unattended), etc)
* Business Analyst - Gets requirements and draws up the inputs and expected outputs of the existing process and of the RPA process
* Implementation Manager - sets up and manages the team working on an RPA initiative and does Availability planning to hit automation goals
* Infrastructure Engineer - sets up and maintains hardware/software (cloud/on-prem orchtestrator, VMs, studio instances, target apps, dev/test/prod environments) resources for RPA dev and Implementation.
* Process Mining Specialist - Use the process mining solution to analyze existing data avail in IT systems and generate the insights necessary to build the automated processes
* Test Automation Specialist - Uses UIPath Studio PRO to design/develop/implement automated testing solutions 