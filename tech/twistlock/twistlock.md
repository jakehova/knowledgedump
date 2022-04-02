# Twistlock

## Background
When using containers, there are three primary challenges that need to be solved to ensure that your deployment is secure: 
1) Access Control - Ensuring that each container follows least-access privelage
2) Inter-Container Communication - Ensuring that communication between containers is secure (authenticated)
3) App within Container - Ensuring that code within your container doesnt violate key security, that exceptions are handled properly, or contain malicious code

Twistlock is a full suite of tools to address those challenges.  

On VA Notify, Twistlock is used to address challenge #3; container scanning.  

## How 
Twistlock is integrated into our CI/CD pipeline. When a developer commits their code to the notify repository, Github triggers a pre-commit hook that launches Twistlock in a github VM environment.  Twistlock then does a scan of the user's commit and the resultant container.  If no issues are found and the container score is above a specified threshold, then the code is committed and Github kicks off any post commit actions.  If there ARE issues found, then the commit is rejected and the dev is notified that an error was found.