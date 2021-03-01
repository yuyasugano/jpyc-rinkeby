#!/usr/bin/python3
import os
from brownie import PriceConsumerV3, accounts, network, config

def main():
    if network.show_active() == 'rinkeby':
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        return PriceConsumerV3.deploy({'from': dev})
    else:
        print('Please pick a supported network, and add your private key')
