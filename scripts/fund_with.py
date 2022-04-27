from brownie import FundMe
from scripts.check import get_account

# 0x9d821ED8C13dDAAE20E31a34B2E7721438B2ed23
def fund():
    account = get_account()
    cont = FundMe[-1]
    entry = cont.getEntry()
    tx = cont.Fund({"from": account, "value": entry})
    tx.wait(1)
    print("Adding $50 to the contract")


def price():
    cont = FundMe[-1]
    pr = cont.getprice()
    print(pr)


def withdraw():
    print("Withdrawing ....")
    cont = FundMe[-1]
    account = get_account()
    cont.withdraw({"from": account})
    print("Total Supply after withdrawl {} ".format(cont.totalFunds()))


def ttlsup():
    cont = FundMe[-1]
    print("Total supply is {}".format(cont.totalFunds()))


def main():
    fund()
    withdraw()
    # ttlsup()
