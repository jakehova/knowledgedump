require("dotenv").config();
const Web3 = require("web3");
const web3 = new Web3(
  new Web3.providers.WebsocketProvider(process.env.INFURA_URL)
);

web3.eth.subscribe("newBlockHeaders")
.on("data", async (block) => {
  console.log(`Block ${block.number} received`, block);
})
.on('error', error => {
    console.error("Error encountered during newBlockHeaders", error)
});
