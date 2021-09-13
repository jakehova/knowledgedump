# Web3

## Basics
* Created by Ethereum Foundation 
* To interact with a contract on the chain you need to message a node: 
  * Requires: 
    * the contract's ABI (Application Binary Interface) that tells Web3 how to interact with the contract.  ABI describes: 
      * the contract's functions
      * the contracts's functions' parameters
* Ethereum nodes speak JSON-RPC.  Web3 abstracts away that low level language.
* **Installation** npm install web3 || yard add web3 || <script language="javascript" type="text/javascript" src="web3.min.js"></script>

## Common functions
* initiate contract - the contract's address of the smart contract you want to communicate with
```
var myContract = new web3js.eth.Contract(myABI, myContractAddress);
```
* get user's account address 
```
var userAccount = web3.eth.accounts[0]
```
  * because a user can change their account at any time, you'll want to check that user account before you carry out any actions that require the user's address.  One way to handle that is to run an interval to update a global value that holds the user account.
```
// initializing 
var userAccount = web3.eth.accounts[0]
// every 100 milliseconds, update the userAccount value and then update the interface accordingly
var accountInterval = setInterval(function() {
  // Check if account has changed
  if (web3.eth.accounts[0] !== userAccount) {
    userAccount = web3.eth.accounts[0];
    // Call some function to update the UI with the new account
    updateInterface();
  }
}, 100);
```
* call - call a view/pure solidity contract function
```
myContract.methods.<method to call>(<parameters to send>).call();
```
* send - creates a transaction and change data on the blockchain.  This requires gas so will open metamask to prompt for payment
  * promise events: 
    * "receipt" - fires when the transaction is included in a block 
    * "error" - fires when theres an issue that prevented the tx from being included in the block
```
myContract.methods.<method to call>(<parameters to send>).send({from: <user account address>, value: <optional but used to send wei to the contract> gas: <optional but is the gas you want to pay for this transaction>})
    .on("receipt", function(receipt) {...})
    .on("error", function(error){...});
```
* convert Ether to wei & make a call to a payable function
```
var convert1EthToWei = web3js.utils.toWei("0.001", "ether");
myContract.methods.payThatManHisMoney().send({from: <user account address>, value: convert1EthToWei})
```
* subscribing to events
```
// monitor for EVERY time the event is thrown (not just the events pertinent to this user)
myContract.events.<event name>()
  .on("data", function(event){
    let vals = event.returnValues;
  })
  .on("error", console.error);
```
  * indexed - when the contract specifies a parameter is indexed, you can filter the event results 
```
// in contract
event Transfer(address indexed _from, address indexed _to, uint256 _tokenId);

// in web3 code
var userAccount = web3.eth.accounts[0]
myContract.events.Transfer({filter: {_to: userAccount}})
  .on("data", function(event){
    let data = event.returnValues;
  })
  .on("error", console.error);
```
* querying past events
```
myContract.getPastEvents("<event name>", { fromBlock: 0, toBlock: "latest", filter: {<indexed param name>: <indexed param value>} })
.then(function(events) {
  // `events` is an array of `event` objects that we can iterate, like we did above
  // This code will get us a list of every zombie that was ever created
});
```

## Tools
* Infura - has APIs that allow you to communicate with Ethereum nodes
* Metamask - allows users securely manage their Ethereum accounts and private keys
    * Code to verify that metamask exists and can be accessed
```
window.addEventListener('load', function() {

  // Checking if Web3 has been injected by the browser (Mist/MetaMask)
  if (typeof web3 !== 'undefined') {
    // Use Mist/MetaMask's provider
    web3js = new Web3(web3.currentProvider);
  } else {
    // Handle the case where the user doesn't have web3. Probably
    // show them a message telling them to install Metamask in
    // order to use our app.
  }

  // Now you can start your app & access web3js freely:
  startApp()
})
```
