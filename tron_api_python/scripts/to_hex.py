import base58

address = "TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F"
hex_address = base58.b58decode_check(address).hex()

print(hex_address)