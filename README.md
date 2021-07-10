# Read Before Installing

For those of you that participated in the testnet I thank you. You will need to completely remove the previous version of Avocado. Delete the .avocado folder and the avocado-blockchain folder.

- Windows: c:\users\%username%\.avocado and c:\users\%username%\AppData\local\avocado-blockchain
- Linux: Wherever you git cloned

## Updates

- Difficulty has been brought down from testnet high. Hopefully a good compromise.
- PNG/SVGs have been updated. I'd give them a C grade. Sorry not a graphic designer.
- rpc_port: 6759 has been changed to rpc_port: 6749 due to conflix with flax - thank you alsipsclar from discord
- Premine is 250,000

## Windows Installation

- https://github.com/Avocado-Network/avocado-blockchain/releases/tag/Mainnet

## Linux Installation

```sh
git clone https://github.com/avocado-network/avocado-blockchain
cd avocado-blockchain
sh install.sh
. ./activate
avocado init
```
## Add Gui
```sh
sh install-gui.sh
cd avocado-blockchain-gui
npm run electron &
```
## Expectations

Most likely the blockchain will be rocky in the beginning. I will have 3 fast timelords running at launch. Please be patient if we experience issues. Of course everyone that participates in Avocado wants it to be worth something but the reality is you could have 1000 AVO and it be worth the same as someone with 0 AVO.


## Why Premine?

I have spent and will continue to spend many hours building Avocado, but time is not the only cost. I also have monthly server costs that go into running the chain. At launch there will be a total of 6 separate servers helping run the chain. I would also like to give back to those that helped with testnet and find fun ways to give back to the community as a whole.

## Nodes

- avocadot1.avocadonetwork.net:6865
- avocadot2.avocadonetwork.net:6865
- avocadot3.avocadonetwork.net:6865

