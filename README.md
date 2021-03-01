# JPYCoin (JPYC) Rinkeby
  
## Overview
  
`JPYC` is a JPY-pegged stablecoin, legally treated as a prepaid payment instrument in Japan. With this said the stablecoin enables us to purchase goods as a medium of exchange. `JPYC` is a simple ERC-20 based token so that we can implement and integrate this token in Ethereum DApps ecosystem. Here is the reason JPYC Rinkeby takes place for testing purpose.
 
To know details about `JPYC`, visit https://jpyc.jp/white-paper-en.pdf
 
## Use of JPYC Rinkeby
 
`JPYC Rinkeby` is a ERC-20 based contract that was deployed at the address [0xbd9c419003a36f187daf1273fce184e1341362c0][jpyc]. Here is the explanation how JPYC Rinkeby works if you want to get some.
 
1. Obtain Rinkeby Eth from one of the faucets to exchange it with JPYC Rinkeby
2. Send Rinkeby Eth to the `JPYC Rinkeby` contract address from your wallet
3. The contract computes how much JPYC should be returned with off-chain data from Chainlink Oracle
4. The contract sends equivalent JPYC to your wallet address at the current rate of ETH/JPY
5. It's time to use JPYC for your testing purpose!! Viola.
 
## Testing
 
The test scripts are stored under the tests directory, it consists of general token test cases from `brownie bake token`.
* __tests/test\_approve.py__: test cases about approve funtion.
* __tests/test\_transferFrom.py: test cases about transferFrom function.
* __tests/test\_transfer.py: test cases about transfer function.
 
```sh
$ brownie --version
Brownie v1.12.4 - Python development framework for Ethereum
$ brownie test
```
 
To get details about `brownie test`, visit https://eth-brownie.readthedocs.io/en/stable/tests-pytest-intro.html
 
## Environment variables
  
When you use `rinkeby` network from `brownie`, you must configure the environment variable `WEB3_INFURA_PROJECT_ID`.
 
[jpyc]: https://rinkeby.etherscan.io/address/0xbd9c419003a36f187daf1273fce184e1341362c0 "JPYC Rinkeby"
