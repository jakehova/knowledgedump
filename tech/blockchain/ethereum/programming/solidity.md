# Solidity

**Notes**
* variables starting with an "_" are local variables and arent stored anywhere in the contract
* Use [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) library of Eth smart contracts to perform common functions (like math functions) 
  * import 'openzeppelin-solidity/contracts/math/SafeMath.sol';
* Refer to the contract address you are in by using this operator: address(this);

**Structure**
* Starts with definition of version "pragma solidity ^0.5.16;"
  * Version number is defined by which version of "solc" truffle is using
* Define the contract by name: contract Election { /* Contract code */ }
* Define the constructor: constructor() public { /* constructor code */ }
* Define variables for contract: string public candidate;
* Define an object: 
```
struct CandidateEntity { 
    uint id; 
    string name;
    uint voteCount;
}
```





    * Generating an instance of an object requires passing all the initial value properties in to the object name => CandidateEntity(1, "Jacob", 0);
* Define a hash (key/value pairs): mapping(uint => CandidateEntity) public candidates;
  * mapping(<key type> => <value type>)
* Data for a contract can be stored in storage (persistent), memory or the stack.  

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