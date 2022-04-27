from brownie import accounts, network, config

forked = ["mainnet-fork-dev"]
LOCAL_ENV = ["ganache-local", "development"]


def get_account():
    if network.show_active() in LOCAL_ENV or network.show_active() in forked:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
