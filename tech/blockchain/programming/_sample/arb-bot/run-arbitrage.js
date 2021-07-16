require("dotenv").config();
const Web3 = require("web3");
const abis = require("./abis");
const { mainnet: addresses } = require("./addresses");

const web3 = new Web3(
  new Web3.providers.WebsocketProvider(process.env.INFURA_URL)
);

const kyber = new web3.eth.Contract(
  abis.kyber.kyberNetworkProxy,
  addresses.kyber.kyberNetworkProxy
);

const AMOUNT_ETH = 100; // compromise btwn low enough to make a profit and high enough to pay for slippage if it occurs
const RECENT_ETH_PRICE = 230;
const AMOUNT_ETH_WEI = web3.utils.toWei(AMOUNT_ETH.toString());
const AMOUNT_DAI_WEI = web3.utils.toWei(
  (AMOUNT_ETH * RECENT_ETH_PRICE).toString()
);

web3.eth
  .subscribe("newBlockHeaders")
  .on("data", async (block) => {
    console.log(`Block ${block.number} received`);

    const kyberResults = await Promise.all([
      kyber.methods
        .getExpectedRate(
          addresses.tokens.dai,
          "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
          AMOUNT_DAI_WEI
        )
        .call(),
      kyber.methods
        .getExpectedRate(
          "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
          addresses.tokens.dai,
          AMOUNT_ETH_WEI
        )
        .call(),
    ]);

    console.log(kyberResults);
  })
  .on("error", (error) => {
    console.error("Error encountered during newBlockHeaders", error);
  });
