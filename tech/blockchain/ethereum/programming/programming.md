Your new key was generated

Public address of the key:   0xF21EacE041411B84be9Ee6227C41Ae96713f05ec
Path of the secret key file: C:\Users\jacob\AppData\Local\Ethereum\keystore\UTC--2021-06-06T14-13-46.534299500Z--f21eace041411b84be9ee6227c41ae96713f05ec

- You can share your public address with anyone. Others need it to interact with you.
- You must NEVER share the secret key with anyone! The key controls access to your funds!
- You must BACKUP your key file! Without the key, it's impossible to access account funds!
- You must REMEMBER your password! Without the password, it's impossible to decrypt the key!

**Tools**
* [REMIX](https://remix.ethereum.org/) - online IDE for Eth contracts
* [Ganache](https://www.trufflesuite.com/ganache) - ETH simulator -> this is not the command line version 
* [Ganache-CLI](https://github.com/trufflesuite/ganache-cli) - ETH simulator that speeds up process of setting up private network and txs are mined immediately
* [GETH](https://geth.ethereum.org/) (Go Ethereum client)  - used to interact with ETH network
  * eth.sendTransaction(): send tx obj.  GETH will help signing tx if it has access to private key
  * eth.sendRawTransaction(): sending serialized signed tx. Used when private key is NOT handled by geth. 
* [Truffle](https://truffleframework.com) - used to develop and test dapps and smart contracts on eth
* [Drizzle](https://www.trufflesuite.com/drizzle) - React library that live updates a redux store with eth data
* [Vanity ETH](https://vanity-eth.tk/) - Get a vanity ETH address to use for sending/receiving items during development
* [Money Legos](https://money-legos.studydefi.com/#/) - 


**Setup**
1) create front end project; npx create-react-app <appname>
   1) update package.json with package-example.json 
2) create truffle project
   1) truffle init
   2) update truffle-config.json: 



3) add .babelrc file with: { "presets": ["es2015", "stage-2", "stage-3"] } 
4) add .env file (accessed via npm package dotenv)
5) smoke test by running truffle compile from command line and confirming that ABI is generated for each contract in contracts folder
6) run truffle migrate to deploy the contracts to the blockchain (defined in truffle-config file)


