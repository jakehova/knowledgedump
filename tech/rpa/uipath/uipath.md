# UI Path

## What
First hyper automation RPA suite 

## How
Process: 
* Discovery
    * UI Path Task Minimg - uses AI to document and analyze front-end process tasks
        * Accessed via UI Path Orchestrator
        * Builds a centralized process map, containing everything from number of steps, clicks and execution time to actual screenshots
        * Provides an RPA score for each task and a report with automation suggestions
    * UI Path Process Mining - monitors and analyzes back-end process logs        
        * Provides data-driven insights to support the prioritization of automatino tasks
    * UI Path Task Capture - Collects essential process details and outputs them as a process definition document or UI Path studio file        
        * Interface that all employees can access and see and submit ideas for automation
        * During submission questions will be asked by task capture to see how possible it is to build an automation out of the process (its scored)
        * Acts as a centralized document repository for each of the ideas 
    * UI Path Automation Hub - Crowdsource Automation ideas from employees and add certain ones to automation pipeline and measure ROI with full transparency    
* Build
    * UI Path Studio - used to build process flows
        * for devs with a programming background who are looking to create complex automation projects
    * UI Path StudioX - used to build process flows in a no code platform
        * for business users who want to create task automation for personal use
        * Resources (applications, excel files, etc) define the scope of your automation.  
        * Project Notebook contains formula cheatsheet and a scratchpad for automation
        * runs the robot as an attended automation 
* Manage
    * UI Path Orchtestrator - Manage users, licensing via on prem install
        * allows grouping of robots and distribution of work items through queues with SLAs
        * Flexible provisioning, Easy Credential Management (works with AD)
        * Has credential store integration
        * High Security/High Availability 
        * Predictive SLAs
        * Open Architecture with large api set
        * Can process monitor
    * UI Path Cloud Platform - Manage users, licensing via UI Path cloud
        * controle human/robot license Management
        * robot provisioning to individual machines
        * distribution of automation processes and tasks to robots
        * monitor and logging 
        * Predictive SLAs
        * Open Architecture with large api set
* Run
    * Robots: 
        * Unattended - should be independent.  If human input is required, robot should be able to continue working until it receives it.
            * Implemented in an architecture led by UI Path Orchestrator.
            * Usually deployed in VMs
            * Can create tasks and distribute them to humans and then continue their work.  When the human input comes, the robots should pick up where they need to.
        * Attended - has an interface that has easy controls and reacts to whatever a human user does.
            * UI Path Assistant is the name of the interface (interface allows for starting, stopping, monitoring, and scheduling with recurrences).
            * Can be setup to monitor actions of human users and start their own actions and run multiple processes in parallel
            * Can be connected to UI Path Orchtestrator to receive the latest process updates automatically
            * Can be instructed to run processes directly from UI Path Orchtestrator
* Engage
    * UI Path Action Center - E2E business processes can be automated through collab between robots and humans.  Robots generate tasks while they are running.  Those tasks can be viewed by the humans.  Analyze Expectations, Escalate, Approve 
    * UI Path Apps - Unattended robots that: 
        * When they reach an intervention point, a Task gets created and assigned then added to the common task list.  
        * When a human enters input in response to that task, a free robot (not necessarily the one that created the task) can resume the automation from where it was handed off to the human user
* Measure
    * UI Path Insights - Primary ROI evaluation tool.  Processing Speed, Volume, Health Indicators.
        * Evaluates and monitors automation results and uses AI to aggregate all data and generate dashboard

## Resources
* (UI Path Connect)[https://connect.uipath.com/]
* (UI Path Form)[https://forum.uipath.com/]
* (UI Path Marketplace)[https://go.uipath.com/]
* (UI Path Academy)[https://academy.uipath.com/lms/]

