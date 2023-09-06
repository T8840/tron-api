import csv

from tronapi import Tron
from utils import address_to_hex
from tronapi.transactionbuilderupdate import CustomTransactionBuilder
from dotenv import dotenv_values

# Read CSV values
def read_csv(filename="./accounts.csv"):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

env_values = dotenv_values()
full_node = env_values["NILE_FULL_NODE"]
tron = Tron(full_node=full_node)
tron.transaction_builder = CustomTransactionBuilder(tron)
signer_account_address = "TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s"
signer_account_address_hex = address_to_hex(signer_account_address)
# Update the permissions
def update_permissions(default_address, private_key):

    tron.private_key = private_key
    tron.default_address = default_address
    default_account_address_hex = address_to_hex(default_address)

    try:
        transaction = tron.transaction_builder.update_account_permissions(
            owner_address=default_account_address_hex,
            owner_permissions={
                "keys": [{"address": signer_account_address_hex, "weight": 1}],
                "threshold": 1,
                "permission_name": "owner",
                "type": 0
            },
            actives_permissions=[
                {
                    'type': 2,
                    'permission_name': 'active',
                    'operations': '7fff1fc0033efb0f000000000000000000000000000000000000000000000000',
                    'threshold': 2,
                    'keys': [
                        {'address': default_account_address_hex, 'weight': 1},
                        {'address': signer_account_address_hex, 'weight': 1}
                    ],
                }],
        )
        signed_tx = tron.trx.sign(transaction)
        result = tron.trx.broadcast(signed_tx)
        return result
    except Exception as e:
        import traceback
        traceback.print_exc()
        return None

# Process each row from the CSV
csv_values = read_csv()
for row in csv_values:
    default_address = row["DEFAULT_ADDRESS"]
    private_key = row["PRIVATE_KEY"]
    update_result = update_permissions(default_address, private_key)
    print(update_result)
