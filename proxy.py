from web3 import Web3

#Slot EIP-1967 proxy (address)
EIP1967_IMPLEMENTATION_SLOT = '0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc'

def has_contract_code(w3: Web3, address: str) -> bool:
    
    #check
    try:
        checksum_address = Web3.toChecksumAddress(address)
        code = w3.eth.get_code(checksum_address)
        return len(code) > 0
    except Exception as e:
        print(f"[Errore] impossible to read {address}: {e}")
        return False

def get_proxy_implementation(w3: Web3, proxy_address: str) -> str | None:
    
    try:
        checksum_address = Web3.toChecksumAddress(proxy_address)
        storage_bytes = w3.eth.get_storage_at(checksum_address, int(EIP1967_IMPLEMENTATION_SLOT, 16))
        if storage_bytes == b'\x00' * 32:
            return None
        #20
        impl_address = Web3.toChecksumAddress("0x" + storage_bytes[-20:].hex())
        return impl_address
    except Exception as e:
        print(f"[Errore] proxy storage.. ops {proxy_address}: {e}")
        return None
