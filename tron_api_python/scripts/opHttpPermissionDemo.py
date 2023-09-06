
import requests
import json
import base58

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

# Define the target address
account_address= 'TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F'
signer_address='TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s'

hex_account_address = base58.b58decode_check(account_address).hex()
hex_signer_address = base58.b58decode_check(signer_address).hex()
# Define the payloads
payload_accountpermissionupdate = {
    "owner_address": "41c6a137bb170cc0dd40fcb83f18b389fa9426ac46",
    "owner": {
        "keys": [{"address": "41c6a137bb170cc0dd40fcb83f18b389fa9426ac46", "weight": 1}],
        "threshold": 1,
        "permission_name": "owner",
        "type": 0
    },
    "actives": {
        "operations": "7fff1fc0033efb0f000000000000000000000000000000000000000000000000",
        "keys": [{"address": "41c6a137bb170cc0dd40fcb83f18b389fa9426ac46", "weight": 1}],
        "threshold": 1,
        "id": 2,
        "type": 2,
        "permission_name": "active"
    }
}
payload_accountpermissionupdate_1 = {
    "owner_address": hex_account_address,
    "owner": {
        "keys": [{"address": hex_account_address, "weight": 1}],
        "threshold": 1,
        "permission_name": "owner",
        "type": 0
    },
    "actives": {
        "operations": "7fff1fc0033efb0f000000000000000000000000000000000000000000000000",
         "keys": [
                {
                    "address": hex_account_address,
                    "weight": 1
                },
                {
                    "address": hex_signer_address,
                    "weight": 1
                }
            ],
        "threshold": 2,
        "id": 2,
        "type": 2,
        "permission_name": "active"
    }
}

payload_accountpermissionupdate_example = {
    "owner_address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
    "actives": [
        {
            "type": 2,
            "permission_name": "active0",
            "threshold": 2,
            "operations": "7fff1fc0037e0000000000000000000000000000000000000000000000000000",
            "keys": [
                {
                    "address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
                    "weight": 1
                },
                {
                    "address": "TPswDDCAWhJAZGdHPidFg5nEf8TkNToDX1",
                    "weight": 1
                }
            ]
        }
    ],
    "owner": {
        "type": 0,
        "permission_name": "owner",
        "threshold": 1,
        "keys": [
            {
                "address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
                "weight": 1
            }
        ]
    },
    "visible": True
}



payload_broadcasttransaction = {
    "visible": False,
    "txID": "4fb2f7e732b6a6f4eb92a60e5fe2f44c77cb6617a6c8ffd80709e9472bc536dc",
    "raw_data": {
        "contract": [{
            "parameter": {
                "value": {
                    "owner": {
                        "keys": [{"address": "41c6a137bb170cc0dd40fcb83f18b389fa9426ac46", "weight": 1}],
                        "threshold": 1,
                        "permission_name": "owner"
                    },
                    "owner_address": "41c6a137bb170cc0dd40fcb83f18b389fa9426ac46",
                    "actives": [{
                        "operations": "7fff1fc0033efb0f000000000000000000000000000000000000000000000000",
                        "keys": [{"address": "41c6a137bb170cc0dd40fcb83f18b389fa9426ac46", "weight": 1}],
                        "threshold": 1,
                        "id": 2,
                        "type": "Active",
                        "permission_name": "active"
                    }]
                },
                "type_url": "type.googleapis.com/protocol.AccountPermissionUpdateContract"
            },
            "type": "AccountPermissionUpdateContract"
        }],
        "ref_block_bytes": "a8ee",
        "ref_block_hash": "5f509422fe567c1c",
        "expiration": 1693878006000,
        "timestamp": 1693877948365
    },
    "raw_data_hex": "0a02a8ee22085f509422fe567c1c40f0e1fc97a6315ad001082e12cb010a3c747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e4163636f756e745065726d697373696f6e557064617465436f6e7472616374128a010a1541c6a137bb170cc0dd40fcb83f18b389fa9426ac4612241a056f776e657220013a190a1541c6a137bb170cc0dd40fcb83f18b389fa9426ac461001224b080210021a06616374697665200132207fff1fc0033efb0f0000000000000000000000000000000000000000000000003a190a1541c6a137bb170cc0dd40fcb83f18b389fa9426ac46100170cd9ff997a631",
    "signature": ["70a991db841e64740f1e3099d5056d45359709df3a5a5a8eb82bbb3a702afe14332660f07cd34ec9bf401f8ba022cb62802a796a488edde775c7d410af41842e00"]
}


# API endpoints
api_url_accountpermissionupdate = "https://api.nileex.io/wallet/accountpermissionupdate"
api_url_broadcasttransaction = "https://api.nileex.io/wallet/broadcasttransaction"

try:
    # Send the requests
    response_accountpermissionupdate = send_request(payload_accountpermissionupdate_1, payload_accountpermissionupdate)
    # response_broadcasttransaction = send_request(api_url_broadcasttransaction, payload_broadcasttransaction)

    # Print the responses
    print("Response for accountpermissionupdate API:", json.dumps(response_accountpermissionupdate, indent=4))
    # print("Response for broadcasttransaction API:", json.dumps(response_broadcasttransaction, indent=4))

except Exception as e:
    print(f"Error: {e}")

