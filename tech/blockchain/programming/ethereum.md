# Programming Ethereum

## NOTES
* 1 ether = 10 ^ 18 wei
    * web3.utils.toWei(<amount of eth>.toString());

## LION method
1) Plan - Develop a strategy (assets, strategies)
2) Observe - monitor assets 
3) Attack - Execute code

## Tools
* NodeJS
* Truffle - used to run solidity contracts 
    * npm install -g truffle 
* Ganache - mock copy of Ethereum blockchain to develop against
* VS Code
* Ethereum Node
    * [Infura](https://infura.io/)
        * Mainnet (USING TESTBOT PROJECT):
            * https://mainnet.infura.io/v3/8f071a3cb552454593b776a86ab5e623
            * wss://mainnet.infura.io/ws/v3/8f071a3cb552454593b776a86ab5e623
        * Kovan
            * https://kovan.infura.io/v3/8f071a3cb552454593b776a86ab5e623
            * wss://kovan.infura.io/ws/v3/8f071a3cb552454593b776a86ab5e623
* Web3
    * npm install web3
    * Initializing web3:
```
const Web3 = require('web3');
// use this if connecting via http*
const web3 = new Web3(<infura http url>)
// use this if connecting via web sockets  
const web3 = new Web3(new Web3.providers.WebsocketProvider('<web socket url>'));
```

## Setting up a Project
* Copy _template/generic-project-setup to working folder
* npm init -y && npm install web3 dotenv --save
* Create entrypoint file: index.js and .env file 
* Put infura url in .env file (INFURA_URL=<infura url>)
* templated code for file
```
require('dotenv').config();
const Web3 = require('web3');
const web3 = new Web3(new Web3.providers.WebsocketProvider(process.env.INFURA_URL));
```


## Where to get ABIs and token addresses
* Go to [Etherscan](https://etherscan.io/) and search 
* Go to documentation for that service and find it there

## Poll Kyber Prices
* Connect to Kyber 
```
const abis = require('./abis');
const { mainnet: addresses } = require('./addresses');

const kyber = new web3.eth.Contract(
    abis.kyber.kyberNetworkProxy,
    addresses.kyber.kyberNetworkProxy
)
```
