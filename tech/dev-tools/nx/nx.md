# NX

**Setup**
* Create new workspace => npx create-nx-workspace@latest
* npm install -g nx


**Running**
*  Serve an application => nx serve <appname>
    * if nx is not installed then => npx nx serve <appname>
    * if you want to run via local installation then => npm run nx --serve <appname>
* Run an e2e => npx nx e2e <e2e project name>

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
