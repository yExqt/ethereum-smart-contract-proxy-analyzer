from web3 import Web3


def checksum_address(addr):
 return Web3.toChecksumAddress(addr)