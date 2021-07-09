# CI/CD via GitHub Actions

## Terms
**Breakdown**: Workflow has Job(s) has Step(s) has Action(s)
"workflow" - unit of automation from start to finish
"job" - section of the workflow that groups steps
"step" - represents ONE effect of the automation.  Could be anotehr Github Action or an actual action like printing to the console.
"action" - the actual piece of automation or code to run. actions/checkout@v2 copies codebase to virtual machine.  actions/setup-node@v2 sets up proper versions of nodejs.


"on" - tells GitHub Actions when to run (i.e. push)
"jobs" - core component of a  Workflow.  Every job needs a specific host machine to run on.  The host to run on is defined in the "runs-on" field. 
"run" - allows you to run cmd line commands in the virtual machine (like npm install)


