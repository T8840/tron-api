import requests
from tron.config import mainAccount , api_chain_url , accounts

# https://developers.tron.network/docs/tron-protocol-transaction

def getTXByAddress(address: str):
    url = api_chain_url + f"/v1/accounts/{address}/transactions"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.text)
    # {"data":[{"ret":[{"contractRet":"SUCCESS","fee":1000000}],"signature":["1ddad0478c0a1c3c12c970cb90ca09446223d634ea5c315768b4c64cf273545a12c186e5de9884117f4933b4635347a38ff8a26d3ab659520adbe60547e071b600"],"txID":"1abdaae882a5bd80bda189e8722705a4b7d110f580da3ad000d0fe53e61b469f","net_usage":268,"raw_data_hex":"0a02fa7322082b2f6684f998649540d0d4d3f9a5315a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a154179309abcff2cf531070ca9222a1f72c4a5136874121541c6a137bb170cc0dd40fcb83f18b389fa9426ac461880b489137092b9f4f7a531","net_fee":0,"energy_usage":0,"blockNumber":54393481,"block_timestamp":1693810770000,"energy_fee":0,"energy_usage_total":0,"raw_data":{"contract":[{"parameter":{"value":{"amount":40000000,"owner_address":"4179309abcff2cf531070ca9222a1f72c4a5136874","to_address":"41c6a137bb170cc0dd40fcb83f18b389fa9426ac46"},"type_url":"type.googleapis.com/protocol.TransferContract"},"type":"TransferContract"}],"ref_block_bytes":"fa73","ref_block_hash":"2b2f6684f9986495","expiration":1693814418000,"timestamp":1693810760850},"internal_transactions":[]}],"success":true,"meta":{"at":1693811443360,"page_size":1}}

def getContractTXByAddress(address: str):
    url = api_chain_url + f"/v1/accounts/{address}/transactions/trc20"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.text)


def opCreateTx(owner_address: str, to_address: str):
    import json
    url = api_chain_url + "/wallet/createtransaction"

    payload = {
        "owner_address": owner_address,
        "to_address": to_address,
        "amount": 1000,
        "visible": True
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    return json.loads(response.text)
    # {"visible":true,"txID":"db059080e3be60fa42b34d9fc6b98c28c42726153ac435bd8dc6cdce6207b7fd","raw_data":{"contract":[{"parameter":{"value":{"amount":1000,"owner_address":"TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s","to_address":"TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F"},"type_url":"type.googleapis.com/protocol.TransferContract"},"type":"TransferContract"}],"ref_block_bytes":"fca0","ref_block_hash":"37f4b24c1e6e2d1b","expiration":1693812489000,"timestamp":1693812431914},"raw_data_hex":"0a02fca0220837f4b24c1e6e2d1b40a8f6ddf8a5315a66080112620a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412310a1541c6a137bb170cc0dd40fcb83f18b389fa9426ac46121541fd4401c8617c503a60d62a0007ae6077620189ca18e80770aab8daf8a531"}
"""

{
    "visible":true,
    "txID":"db059080e3be60fa42b34d9fc6b98c28c42726153ac435bd8dc6cdce6207b7fd",
    "raw_data":{
        "contract":[
            {
                "parameter":{
                    "value":{
                        "amount":1000,
                        "owner_address":"TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s",
                        "to_address":"TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F"
                    },
                    "type_url":"type.googleapis.com/protocol.TransferContract"
                },
                "type":"TransferContract"
            }
        ],
        "ref_block_bytes":"fca0",
        "ref_block_hash":"37f4b24c1e6e2d1b",
        "expiration":1693812489000,
        "timestamp":1693812431914
    },
    "raw_data_hex":"0a02fca0220837f4b24c1e6e2d1b40a8f6ddf8a5315a66080112620a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412310a1541c6a137bb170cc0dd40fcb83f18b389fa9426ac46121541fd4401c8617c503a60d62a0007ae6077620189ca18e80770aab8daf8a531"
}
"""

def opBroadcastTx(raw_data, raw_data_hex):
    url = api_chain_url +  "/wallet/broadcasttransaction"

    payload = {
        "raw_data":raw_data ,
        "raw_data_hex":raw_data_hex,
        "privateKey": private_key
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)



def opTran():
    import requests
    import json

    # 定义Tron API的URL和要使用的钱包地址和私钥
    api_url = "https://api.trongrid.io/wallet/createtransaction"
    wallet_address = "TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s"
    private_key = ""
    to_address = "TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F"
    amount = 1000  # 要转账的金额

    # 构建转账数据
    payload = {
        "to_address": to_address,
        "owner_address": wallet_address,
        "amount": amount
    }

    # 发送POST请求来创建转账交易
    response = requests.post(api_url, json=payload)
    print(response.text)
    # 检查请求是否成功
    if response.status_code == 200:
        response_json = response.json()

        # 检查转账交易是否创建成功
        if response_json["result"]:
            transaction = response_json["transaction"]
            transaction["visible"] = True

            # 签名转账交易
            signed_transaction = {
                "transaction": transaction,
                "privateKey": private_key
            }

            # 发送POST请求来广播已签名的转账交易
            broadcast_url = "https://api.trongrid.io/wallet/broadcasttransaction"
            response = requests.post(broadcast_url, json=signed_transaction)

            # 检查转账是否成功广播
            if response.status_code == 200:
                response_json = response.json()

                if response_json["result"]:
                    print("转账成功！")
                else:
                    print("转账失败：", response_json["message"])
            else:
                print("转账广播失败：", response.status_code)
        else:
            print("创建转账交易失败：", response_json["message"])
    else:
        print("创建转账交易请求失败：", response.status_code)


if __name__ == "__main__":
    # getTXByAddress(mainAccount)
    # getContractTXByAddress(mainAccount)
    accounts_list = list(accounts.keys())
    resp = opCreateTx(accounts_list[0], accounts_list[1])
    print(resp.get("raw_data"),resp.get("raw_data_hex"))
    opBroadcastTx(resp.get("raw_data"), resp.get("raw_data_hex"))

