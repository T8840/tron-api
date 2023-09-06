

from tronapi import Tron

import requests
import json

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
to_account_address = "TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s"


request_url = full_node + "/wallet/createtransaction"

def send_request(api_url, payload):
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)

    # Error handling for non-200 responses
    if response.status_code != 200:
        raise Exception(f"API returned {response.status_code}: {response.text}")

    return response.json()


payload = {
    "owner_address": default_account_address,
    "to_address": to_account_address,
    "amount": 1000,
    "visible": True
}


transaction_resp = send_request(request_url, payload)
print("Response for transaction API:", json.dumps(transaction_resp, indent=4))

# 对交易进行签名
signed_transaction = tron.trx.sign(transaction_resp)

# 打印签名结果
print(signed_transaction['signature'])