# NX

[NX Dev](https://nx.dev)

**Setup**
* Create new workspace => npx create-nx-workspace@latest
* npm install -g nx

**Common Commands**
* Platforms: 
  * angular
  * react
  * nest:application    
    * Need to add the plugin before creating application via => npm install --save-dev @nrwl/nest
  * express
* Add Application
  * nx g @nrwl/<platform> <project name>
* Add Library
  * nx g @nrwl/<platform>:lib <library name>
    * To create a standard typescript library: platform is node
* Add Component (Angular)
  * nx g component <componentname> --project=<nameOfProject> --export
* Building
  * nx build <app name> --configuration=<configuration name, defaults to dev>
* Removing a Library or project
  * nx g @nrwl/workspace:remove <library name>
* Running
  * nx serve <app name>
* Run Unit Tests 
  * nx test <app name>

**Workspace Generators**
*  Used to automate tasks that are regularly performed as part of the dev workflow.
*  To add generator => nx generate @nrwl/workspace:workspace-generator <generator name>
      * Creates generator file under tools/generators

**NX CLI vs Angular CLI**
* internally, nx cli delegates to angular cli when running commands or generating code.  
* using nx supports more advanced capabailities that are not supported by angular cli
    * nx cli uses advanced code analysis and computation caching to reuse previous computation results when possible which results in much faster commands vs using angular cli.  
    * nx cli can run a target against many projects in parallel 
    * nx cli can run a target against a project and its dependencies
* nx workspace contains a decorate-angular-cli.js file which remaps ng to invoke nx.  This forces use of nx even when using the ng context.
* nx uses Jest instead of Karma for e2e testing

**Notes**
* When creating a new library in VS Code may be necessary to restart TS Server:
    * Ctrl+Shift+P, type restart, Restart TS Server
* To create a proxy api project pass the "frontendProject" parameter with a value = app to create proxy for:
  * app is named "client-front-end"
  * nx g @nrwl/nest:application client-proxy --frontendProject client-front-end
  * How this works: 
    * Updates workspace.json (if React project) or angular.json (if angular project) to update serve options configuration
      * Adds to serve options config: "proxyConfig":<apps/<pathToApp>/proxy.config.json>
      * adds proxy.config.json file to that app
      * proxy.conf.json file contains endpoint configuration for the proxy
        * { "/api": { "target": "http://localhost:3333, "secure":false}}
