# Algorand SDK

**Create Account**
* [Javascript SDK](https://github.com/algorand/js-algorand-sdk)
```
const algosdk = require('algosdk');

function generateAlgorandKeyPair() {
    var account = algosdk.generateAccount();
    var passphrase = algosdk.secretKeyToMnemonic(account.sk);
    console.log( "My address: " + account.addr );
    console.log( "My passphrase: " + passphrase );
}
```