import argparse
from web3 import Web3

#pars CLI
parser = argparse.ArgumentParser(description="check")
parser.add_argument('--rpc', required=True, help="url eth (es. Infura, Alchemy)")
parser.add_argument('--address', required=True, help="address")
args = parser.parse_args()

#connection1 
w3 = Web3(Web3.HTTPProvider(args.rpc))
contract_address = args.address

from proxy_detector import has_contract_code, get_proxy_implementation
#check2
is_contract = has_contract_code(w3, contract_address)
implementation_address = get_proxy_implementation(w3, contract_address)

#output
print(f"address: {contract_address}")
print(f"yes, contract: {is_contract}")
print(f"proxy c: {implementation_address}")
