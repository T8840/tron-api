from tronapi import Tron
from utils import address_to_hex
from tronapi.transactionbuilderupdate import CustomTransactionBuilder
from dotenv import dotenv_values

env_values = dotenv_values()
full_node = env_values["NILE_FULL_NODE"]
tron = Tron(full_node=full_node)
# Use your custom subclass
tron.transaction_builder = CustomTransactionBuilder(tron)
default_account_address = "TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F"
tron.private_key = env_values["PRIVATE_KEY"]
tron.default_address = default_account_address
default_account_address_hex = address_to_hex(default_account_address)
signer_account_address = "TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s"
signer_account_address_hex = address_to_hex(signer_account_address)

# Update the permissions
def update_permissions():
    try:
        transaction = tron.transaction_builder.update_account_permissions(
            owner_address= default_account_address_hex ,
            owner_permissions= {
                "keys": [{"address": signer_account_address_hex, "weight": 1}],
                "threshold": 1,
                "permission_name": "owner",
                "type": 0
            },
            actives_permissions=
                [{
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

        print("---------signed_tx:------",signed_tx)
        result = tron.trx.broadcast(signed_tx)

        return result
    except Exception as e:
        import traceback
        traceback.print_exc()
        return None


# Update permissions
update_result = update_permissions()
print(update_result)


