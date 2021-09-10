# Web3

## Basics
* Created by Ethereum Foundation 
* To interact with a contract on the chain you need to message a node and tell it: 
    * address of the smart contract you want to communicate with
    * function you want to call
    * variables you want to pass to that function
* Ethereum nodes speak JSON-RPC.  Web3 abstracts away that low level language.
* **Installation** npm install web3 || yard add web3 || <script language="javascript" type="text/javascript" src="web3.min.js"></script>

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
