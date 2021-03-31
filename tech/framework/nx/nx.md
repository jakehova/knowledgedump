# NX

[NX Dev](https://nx.dev)



**Common Commands**
* Platforms: 
  * angular
  * react
  * nest:application    
    * Need to add the plugin before creating application via => npm install -D @nrwl/nest
  * express
* Add Application
  * nx g @nrwl/<platform> <project name>
* Add Library
  * nx g @nrwl/<platform>:lib <library name>
* Add Component (Angular)
  * nx g component <componentname> --project=<nameOfProject> --export
* Building
  * nx build <app name> --configuration=<configuration name, defaults to dev>
* Running
  * nx serve <app name>

**Notes**
* To create a proxy api project pass the "frontendProject" parameter with a value = app to create proxy for:
  * app is named "client-front-end"
  * nx g @nrwl/nest:application client-proxy --frontendProject client-front-end
  * How this works: 
    * Updates workspace.json (if React project) or angular.json (if angular project) to update serve options configuration
      * Adds to serve options config: "proxyConfig":<apps/<pathToApp>/proxy.config.json>
      * adds proxy.config.json file to that app
      * proxy.conf.json file contains endpoint configuration for the proxy
        * { "/api": { "target": "http://localhost:3333, "secure":false}}