# Testing 

## Non-Local Test Networks
* Ropsten: The official test network, created by The Ethereum Foundation. Its functionality is similar to the MainNet.
* Kovan: A network that uses a consensus method called "proof-of-authority". This means its transactions are validated by select members, leading to a consistent four second block time. The supply of ether on this testnet is also controlled to mitigate spam attacks.
* Rinkeby: A testnet also using proof-of-authority, created by The Ethereum Foundation.

## Important Notes
* Run a test: truffle test
* every time we call "contract.new()" truffle deploys a new contract 
* to skip a test put an "x" before the "it" or "context" keywords (i.e. xit or xcontext)
* use "response.logs[0].args.<param name>" to access object parameters that are returned from the contract

## Local-Dev Test
[[.\setting-local-dev]]

## Basics
* During Soliidty compilation, the JSON equivalents are created. 
    * When you run a migration using truffle, truffle will update the JSON file with information related to the network being deployed to
* To write a test, you need to interact with those build artifcats
```
const mycontract = artifacts.require("<name of contract>");
```
* When writing test: 
  * Group tests using "contract("<description>", (<accounts listing>) => {})" => this is the equivalent of "describe" in regular front end tests
```
contract("Test the Deal", (accounts) => {

})
```
  * Describe the test using "it(<description>, ()=>{})"
```
const CryptoZombies = artifacts.require("CryptoZombies");
contract("CryptoZombies", (accounts) => {
    //1. initialize `alice` and `bob`
    it("should be able to create a new zombie", () => { //2 & 3. Replace the first parameter and make the callback async
    })
})
```
* use beforeEach and afterEach to run one time setup code and cleanup respectively: 
```
const CryptoZombies = artifacts.require("CryptoZombies");
const zombieNames = ["Zombie 1", "Zombie 2"];
contract("CryptoZombies", (accounts) => {
    let [alice, bob] = accounts;

    // start here
    let contractInstance;
    beforeEach(async () => {
        contractInstance = await CryptoZombies.new();
    })

    it("should be able to create a new zombie", async () => {

        const result = await contractInstance.createRandomZombie(zombieNames[0], { from: alice });
        assert.equal(result.receipt.status, true);
        assert.equal(result.logs[0].args.name, zombieNames[0]);
    })

    //define the new it() function
    it("should not allow two zombies", async () => {})

    afterEach(async () => {
        await contractInstance.kill();
    })
})
```
* testing for error, use a utility function: 
```
// utility function file
async function shouldThrow(promise) {
  try {
      await promise;
     assert(true);
  }
  catch (err) {
      return;
  }
assert(false, "The contract did not throw.");

}

module.exports = {
  shouldThrow,
};

// test file.
const utils = require("./helpers/utils");
await utils.shouldThrow(contractInstance.createRandomZombie(zombieNames[1], {from: alice}));
```
* use "context" to group tests
```
context("with the single-step transfer scenario", async () => {
    it("should transfer a zombie", async () => {
      // TODO: Test the single-step transfer scenario.
    })
})

context("with the two-step transfer scenario", async () => {
    it("should approve and then transfer a zombie when the approved address calls transferFrom", async () => {
      // TODO: Test the two-step scenario.  The approved address calls transferFrom
    })
    it("should approve and then transfer a zombie when the owner calls transferFrom", async () => {
        // TODO: Test the two-step scenario.  The owner calls transferFrom
     })
})
```

* Run the test: truffle test

