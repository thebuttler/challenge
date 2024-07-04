from web3 import Web3

# temporary bad use of url this should be stored in a environment variable
def get_eth_balance(eth_address):
    infura_url = "https://mainnet.infura.io/v3/c1dfef79061946b28035cda7c0545aab"
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Ensure connection is sucessful
    if not web3.is_connected():
        raise Exception("Failed to connecto the Eth node.")
    
    # Fetch the balance in Wei & convert it to eth
    balance_wei = web3.eth.get_balance(eth_address)
    balance_eth = web3.from_wei(balance_wei, 'ether')

    return balance_eth