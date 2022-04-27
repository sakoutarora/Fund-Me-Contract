from brownie import FundMe, config, network, MockV3Aggregator
from scripts.check import get_account, LOCAL_ENV
from web3 import Web3

DECIMALS = 8
START_PRICE = 200000000000


def main():
    account = get_account()
    if network.show_active() not in LOCAL_ENV:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print("----- Using Mocks -----")
        if len(MockV3Aggregator) <= 0:
            print("Deploying Mock for Dev network .... ")
            price_feed_address = MockV3Aggregator.deploy(
                DECIMALS, START_PRICE, {"from": account}
            )
            price_feed_address = price_feed_address.address
            print("---- Mock Deployed -----")
        else:
            price_feed_address = MockV3Aggregator[-1].address

    fundme = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    return fundme
