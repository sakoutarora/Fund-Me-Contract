from brownie import accounts
from scripts.check import get_account
from scripts.deploy import main


def test_adding():
    cont = main()
    account = get_account()
    val = cont.getEntry() + 1e5
    cont.Fund({"from": account, "value": val})
    assert cont.byAdd(account) == val


def test_witdraw():
    cont = main()
    account = get_account()
    val = cont.getEntry() + 1e5
    cont.Fund({"from": account, "value": val})
    cont.withdraw({"from": account})
    assert cont.totalFunds() == 0
