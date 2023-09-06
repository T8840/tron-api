import requests

def opCreateAccount(owner_address: str, account_address: str):
    url = 'https://nile.trongrid.io' + f"/wallet/createaccount"
    payload = {
        "owner_address": owner_address,
        "account_address": account_address,
        "visible": True
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


if __name__ == "__main__":
    accounts_list = list(accounts.keys())
    opCreateAccount(accounts_list[0],accounts_list[1])
    # print(accounts_list[1])