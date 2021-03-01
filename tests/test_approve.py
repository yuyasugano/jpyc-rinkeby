#!/usr/bin/python3

import pytest

@pytest.mark.parametrize("idx", range(5))
def test_initial_approval_is_zero(token, accounts, idx):
    assert token.allowance(accounts[0], accounts[idx]) == 0

def test_approve(token, accounts):
    amount = 1000 * 1e18
    token.approve(accounts[1], amount, {'from': accounts[0]})
    assert token.allowance(accounts[0], accounts[1]) == amount

def test_modify_approve(token, accounts):
    amount = 1000 * 1e18
    modified = 1234
    token.approve(accounts[1], amount, {'from': accounts[0]})
    token.approve(accounts[1], modified, {'from': accounts[0]})

    assert token.allowance(accounts[0], accounts[1]) == modified

def test_revoke_approve(token, accounts):
    amount = 1000 * 1e18
    token.approve(accounts[1], amount, {'from': accounts[0]})
    token.approve(accounts[1], 0, {'from': accounts[0]})

    assert token.allowance(accounts[0], accounts[1]) == 0

def test_approve_self(token, accounts):
    amount = 1000 * 1e18
    token.approve(accounts[0], amount, {'from': accounts[0]})
    assert token.allowance(accounts[0], accounts[0]) == amount

def test_only_affects_target(token, accounts):
    amount = 1000 * 1e18
    token.approve(accounts[1], amount, {'from': accounts[0]})
    assert token.allowance(accounts[1], accounts[0]) == 0

def test_returns_true(token, accounts):
    amount = 1000 * 1e18
    tx = token.approve(accounts[1], amount, {'from': accounts[0]})
    assert tx.return_value is True

def test_approval_event_fires(accounts, token):
    amount = 1000 * 1e18
    tx = token.approve(accounts[1], amount, {'from': accounts[0]})

    assert len(tx.events) == 1
    assert tx.events["Approval"].values() == [accounts[0], accounts[1], amount]
