#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def token(JPYC, accounts):
    jpyc =  JPYC.deploy({'from': accounts[0]})
    accounts[0].transfer(jpyc.address, "1 ether", gas_price=0)
    accounts[1].transfer(jpyc.address, "1 ether", gas_price=0)
    yield jpyc
    # balance = jpyc.balanceOf(accounts[0]);
    # assert balance > 0, 'account was not able to receive JPYC properly'
