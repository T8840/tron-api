import requests

url = "https://api.shasta.trongrid.io/wallet/accountpermissionupdate"

payload = {
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
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)