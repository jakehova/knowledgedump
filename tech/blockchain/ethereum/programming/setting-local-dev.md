# Setting up a Local Dev Environment

## Basics
**Install truffle** - used to compile your solidity code
```
npm install -g truffle
```
Create a truffle project: 
```
truffle init
```

* Can also use starter sets by using [Truffle Boxes](https://www.trufflesuite.com/boxes)
* Generates: 
    * truffle-config.js - truffle configuration file
    * contracts folder - holds contracts
    * migrations folder - scriptable deployment files
    * test - test files for your application and contracts
Compile Contracts
```
truffle compile
```
**install ganache** - used to run a fake ethereum chain on your local machine
```
npm install -g ganache-cli
```
* run ganache
```
ganache-cli
```
**install ipfs** - used for distributed storage
```
npm install -g ipfs
```
* run ipfs local-dev instance
```
jsipfs daemon
```
## Tools
* [REMIX](https://remix.ethereum.org/) - online IDE for Eth contracts
* [Ganache](https://www.trufflesuite.com/ganache) - ETH simulator -> this is not the command line version 
* [Ganache-CLI](https://github.com/trufflesuite/ganache-cli) - ETH simulator that speeds up process of setting up private network and txs are mined immediately
* [GETH](https://geth.ethereum.org/) (Go Ethereum client)  - used to interact with ETH network
  * eth.sendTransaction(): send tx obj.  GETH will help signing tx if it has access to private key
  * eth.sendRawTransaction(): sending serialized signed tx. Used when private key is NOT handled by geth. 
* [Truffle](https://truffleframework.com) - used to develop and test dapps and smart contracts on eth
* [Drizzle](https://www.trufflesuite.com/drizzle) - React library that live updates a redux store with eth data

## Setup
1) create front end project; npx create-react-app <appname>
   1) update package.json with package-example.json 
2) create truffle project
   1) truffle init
   2) update truffle-config.json: 



3) add .babelrc file with: { "presets": ["es2015", "stage-2", "stage-3"] } 
4) add .env file (accessed via npm package dotenv)
5) smoke test by running truffle compile from command line and confirming that ABI is generated for each contract in contracts folder
6) run truffle migrate to deploy the contracts to the blockchain (defined in truffle-config file)

## Fork Mainnet - Development Environment
- install node/npm 
- npm install ganache-cli -g 
- start ganache at a specific block: ganache-cli -f https://mainnet.infura.io/v3/<infura-api-key> 
- setup metamask to work with the ganache cli: 
    go to metamask ->
    setup custom rpc: http://localhost:8545
    chain id: 1337
    current symbol: eth
    swithc network go to ganache cli 
    import 1 of the private addresses from ganache 
- go to remix -> compile using compiler 0.5.16 solidity compiler 
- go to remoix -> deploy -> injected web 3(metamask) -> select the contract you compiled
    - to borrow ether from dydx -> need to wrap the ETH to make it WETH -> need to pay a small fee  (i.e. borrow 1000 ETH need to pay 0.00000000000000000001 ETH)
        - this 1 WEI (.000000000000000001 ETH) dydx tx fee needs to be sent to contract so that the contract can take out the flash loan


**Migrations via Truffle**
* preceeded with a number that defines the order that truffle runs the migratinos in
* run "truffle migrate" from command line in project directory to run the migration
  * should only be run once since state is immutable
  * "truffle migrate --reset" -> will reset the state of the existing contract and will deploy a new contract with a new address

**Using Truffle Console**
* run "truffle console" to enter into truffle console
* in console, can access variables defined in migrations files
  * example: Election.deployed().then(function(instance) { app = instance }) => will yield "undefined" at console but generates an app variable that is associated with the deployed Election contract defined in the migrations
* Once app is defined, can interact wiht 
  * Get the contract address: app.address
  * Get a variable value: app.<variable name>() => e.g. app.candidate()
    * this returns a promise, so need to use then to get the actual value: 
      * app.candidate().then(function(candidateEntityValue){ candidate = candidateEntityValue});
        * this will allow you to see the candidate using "candidate".  
  * To convert a variable to a number use the "toNumber()" method: candidateCount.toNumber()


**Testing Contracts with JS** - Truffle comes bundled with mocha and chai
* Run Ganache
```
var Election = artifacts.require("./Election.sol");
contract("Election", function(accounts){
    it("initializes with two candidates", function(){
        return Election.deployed().then(function(instance){
            return instance.candidatesCount();
        }).then(function(count){
            assert.equal(count, 2);
        })
    })
}) ;
```
