## Truffle

**Purpose**
* used to run a local eth instance

**Truffle Commands**
* truffle init - generate contracts and config file
  * update package.json: 
    * npm install --save dotenv

```
require("babel-register");
require("babel-polyfill");
require("dotenv").config();

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1", // Localhost (default: none)
      port: 7545, // Standard Ethereum port (default: none)
      network_id: "*", // Any network (default: none)
    },
  },
  contracts_directory: "./src/contracts/",
  contracts_build_directory: "./src/abis/",  
  mocha: {
    // timeout: 100000
  },  
  compilers: {
    solc: {
      version: "0.5.1", // Fetch exact version from solc-bin (default: truffle's version)
      // docker: true,        // Use "0.5.1" you've installed locally with docker (default: false)
      settings: {
        optimizer: {
          enabled: true,
          runs: 200,
        },
      },
    },
  },
  db: {
    enabled: false,
  },
};
```

* truffle compile - compile contracts
* truffle migrate - deploy migrations 
  * migrations are in migrations folder and are executed in the numbering order so file name is important
* truffle console
* truffle test <(optional) specific file>
* truffle exec <file to scripting file>


**Truffle Console**
* const <contract> = await <ContractName>.deployed()
  * <contract>.address will return address of deployed contract;

**Truffle Templates**
* Using: truffle unbox pet-shop -> running that will generate a sandbox dev environment
    * Generates: base skeletorn for building a dapp
      * contracts folder where smart contracts live
        * holds one contract Migrations.sol which handles migrations of all contracts at deployed
      * migrations: all migrations files reside here
      * node_modules
      * src: client side code
      * test: where all test files go 