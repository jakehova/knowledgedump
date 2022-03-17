# Reach

**What**
* Higher level programming langauge for developing against blockchains
* Abstracts away details of underlying consensus network
  * generates smart contract,
  * backend in rsh
  * frontend in mjs
  * deploys it
* [Website](https://reach.sh/)
* [Documentation](https://docs.reach.sh/)

**Installation on Windows**
* [Instructions](https://docs.reach.sh/guide-windows.html)
* Need make, docker and docker-compose
* make is not native to windows so need to use windows subsystem 
* Enable Windows Subsystem for Linux (version 2)
* Download [Docker Desktop](https://www.docker.com/products/docker-desktop) and enable [Docker Desktop WSL 2 backend](https://docs.docker.com/docker-for-windows/wsl/)
* Install VS Code
* Install the [Remote-WSL extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
* Open Powershell and switch to wsl by typing "wsl" command at prompt
* Make a directory for reach off the root and change into it: mkdir -p ~/reach/tut && cd ~/reach/tut
* install reach: curl https://raw.githubusercontent.com/reach-sh/reach-lang/master/reach -o reach ; chmod +x reach
* verify installation: "./reach version"
* update installation: "./reach update"
* build help directory: "./reach compile --help"
* Install [Reach IDE extension](https://marketplace.visualstudio.com/items?itemName=reachsh.reach-ide)
  

**Basics**
* Reach files end in ".rsh"
* Frontend file end in ".mjs"
* 


**Programming**
* initialize a project with: "./reach init" 
  * This creates the index.rsh and index.mjs file
* Code files begin with the version of reach to use: "'reach 0.1';"
* Need to define the main export of the program: 
```
export const main = Reach.App(
   {}, 
   [Participant('<A>', {}), Participant('<B>', {})],
   (<var created for A>, <var created for B>) => {})
```
  * First {} is 
  * First [] specifies the participants.  Each participant has:
    * name, which is first parameter
    * interface definition, which is second parameter
      * this defines what methods/properties are available for this participant
  * lamda parameters are var representations of the participants with the logic being the body of the lambda
* Special terms: 
  * only => extension method to Participant Entity
  * interact => Used in lambda to  execute retrieval of a Participant interface method/value
    * eg: interact.wager or interact.getHand()
  * declassify => Used in lambda defining interaction with the front end
    * Passed a property or method of the Participant interface to get the value/function from
    * eg: declassify(interact.wager)
  * publish => publishes variables to the consensus network.  extension method to Participant Entity: 
    * eg: [Participant('Alice', AliceInterface)], (Alice) => Alice.publish(<values>)
  * pay => chain method off of publish which is used when passing of tokens is required
    * the variable passed into pay must be in publish as well
    * eg: Alice.publish(wager).pay(wager)
  * commit => method that commits publish contents to the network
  * transfer(<number>).to(<Participant Entity>) => Transfers a value to a participant
  * unknowable(<ParticipantA>, <ParticipantB(<var value>)>) => States what ParticipantA cant know at this point in the program
* Best Practices
  * **Always** add an assertion to your program that would fail to hold if the attack or failure were present

* Testing: 
* require(<expression>) => 
  

