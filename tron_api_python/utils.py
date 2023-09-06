import base58

def address_to_hex(address):
    decoded_bytes = base58.b58decode_check(address)
    hex_address = decoded_bytes.hex()
    return hex_address