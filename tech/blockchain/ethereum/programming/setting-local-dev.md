# Setting up a Local Dev Environment

* Use [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) library of Eth smart contracts to perform common functions (like math functions) 
  * import 'openzeppelin-solidity/contracts/math/SafeMath.sol';
  
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
