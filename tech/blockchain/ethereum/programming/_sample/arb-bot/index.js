require('dotenv').config()
const Web3 = require('web3');
const { ChainId, Token, TokenAmount, Pair } = require('@uniswap/sdk');
const abis = require('./abis');
const { mainnet: addresses } = require('./addresses');

const web3 = new Web3(
  new Web3.providers.WebsocketProvider(process.env.INFURA_URL)
);

web3.eth.accounts.wallet.add(process.env.PRIVATE_KEY);

const kyber = new web3.eth.Contract(
  abis.kyber.kyberNetworkProxy,
  addresses.kyber.kyberNetworkProxy
);


const AMOUNT_ETH = 100;   // arbitrage amount goal
const RECENT_ETH_PRICE = 2300; // current price of ETH
const AMOUNT_ETH_WEI = web3.utils.toWei(AMOUNT_ETH.toString()); // convert how much ETH we want to earn to WEI
const AMOUNT_DAI_WEI = web3.utils.toWei((AMOUNT_ETH * RECENT_ETH_PRICE).toString());  // convert the total dollar value of the ETH we want to gain to WEI

const init = async () => {
  const [dai, weth] = await Promise.all(
    [addresses.tokens.dai, addresses.tokens.weth].map(tokenAddress => (
      Token.fetchData(
        ChainId.MAINNET,
        tokenAddress,
      )
  )));

  const daiWeth = await Pair.fetchData(
    dai,
    weth,
  );

  web3.eth.subscribe('newBlockHeaders')
    .on('data', async block => {
      console.log(`New block received. Block # ${block.number}`);

      // find out what the exchange prices are for the pair that we are checking
      const kyberResults = await Promise.all([
          kyber               // returns rate in eth. 
            .methods
            .getExpectedRate(
              addresses.tokens.dai,   // address of source token (token we are buying in)
              '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', // address of destination token (currency we are exchanging to (ETH.  Since ETH doesnt have an address, this is a stand in special value for it))
              AMOUNT_DAI_WEI  // amount of source token we want to use to buy the destination token
            ) 
            .call(),
          kyber             // returns rate in dai 
            .methods
            .getExpectedRate(
              '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 
              addresses.tokens.dai, 
              AMOUNT_ETH_WEI
            ) 
            .call()
      ]);

      // kyber rates are scaled up by 10 ^ 18 (this is done to get rid of decimals).  
      //    so essentially the amount returned is in wei but multipled by 10^18 to make it a whole number
      // convert the rates receievd above into their true wei value.  
      const kyberRates = {
        buy: parseFloat(1 / (kyberResults[0].expectedRate / (10 ** 18))),
        sell: parseFloat(kyberResults[1].expectedRate / (10 ** 18))
      };
      console.log('Kyber ETH/DAI');
      console.log(kyberRates);

      const uniswapResults = await Promise.all([
        daiWeth.getOutputAmount(new TokenAmount(dai, AMOUNT_DAI_WEI)),
        daiWeth.getOutputAmount(new TokenAmount(weth, AMOUNT_ETH_WEI))
      ]);
      // uniswap rates are scaled up by 10 ^ 18 (this is done to get rid of decimals).  
      //    so essentially the amount returned is in wei but multipled by 10^18 to make it a whole number
      // convert the rates receievd above into their true wei value.  
      const uniswapRates = {
        buy: parseFloat( AMOUNT_DAI_WEI / (uniswapResults[0][0].toExact() * 10 ** 18)),
        sell: parseFloat(uniswapResults[1][0].toExact() / AMOUNT_ETH),
      };
      console.log('Uniswap ETH/DAI');
      console.log(uniswapRates);

      const gasPrice = await web3.eth.getGasPrice();
      console.log(`Gas Price: ${gasPrice}`);
      //200000 is picked arbitrarily, have to be replaced by actual tx cost in next lectures, with Web3 estimateGas()
      const txCost = 200000 * parseInt(gasPrice);
      const currentEthPrice = (uniswapRates.buy + uniswapRates.sell) / 2; 
      // (parseInt(AMOUNT_ETH_WEI) / 10 ** 18) => take the pure profit and multiple it by how much min profit we are looking for
      // (uniswapRates.sell - kyberRates.buy) => pure profit
      // - (txCost / 10 ** 18) => include txCost and convert it to ETH
      // *currentEthPrice => want to see the txCost in the current ETH price 
      const profit1 = (parseInt(AMOUNT_ETH_WEI) / 10 ** 18) * (uniswapRates.sell - kyberRates.buy) - (txCost / 10 ** 18) * currentEthPrice;
      const profit2 = (parseInt(AMOUNT_ETH_WEI) / 10 ** 18) * (kyberRates.sell - uniswapRates.buy) - (txCost / 10 ** 18) * currentEthPrice;
      if(profit1 > 0) {
        console.log('Arb opportunity found!');
        console.log(`Buy ETH on Kyber at ${kyberRates.buy} dai`);
        console.log(`Sell ETH on Uniswap at ${uniswapRates.sell} dai`);
        console.log(`Expected profit: ${profit1} dai`);
        //Execute arb Kyber <=> Uniswap
      } else if(profit2 > 0) {
        console.log('Arb opportunity found!');
        console.log(`Buy ETH from Uniswap at ${uniswapRates.buy} dai`);
        console.log(`Sell ETH from Kyber at ${kyberRates.sell} dai`);
        console.log(`Expected profit: ${profit2} dai`);
        //Execute arb Uniswap <=> Kyber
      }
    })
    .on('error', error => {
      console.log(error);
    });
}
init();

