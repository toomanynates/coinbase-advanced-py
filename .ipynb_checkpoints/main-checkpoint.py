from coinbase.rest import RESTClient
import json
from json import dumps
from os import listdir
from os.path import isfile, join
import math
import pandas as pd


#with open('C:\Users\tooma\OneDrive\Desktop\py4e\coinbase_cloud_api_key.json') as user_file:
#    file_contents = user_file.read()
#    parsed_json = json.loads(file_contents)
#    print(parsed_json)

"""
mypath = "C:/Users/tooma/OneDrive/Desktop/py4e/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles) #['code.txt', 'coinbase_cloud_api_key.json', 'coinbase_cloud_api_key.zip', 'first.py', 'get-pip.py', 'py', 'Python 3.12 (64-bit).lnk', 'Visual Studio Code.lnk']
"""

try:
   file = open("C:/Users/tooma/OneDrive/Desktop/py4e/coinbase_cloud_api_key.json", "r")
#   print(file.read())
   data = json.load(file)

   print(data["name"])
   print(data["privateKey"])

   api_key = data["name"]
   api_secret = data["privateKey"]
   
   client = RESTClient(api_key=api_key, api_secret=api_secret)
   client.get
   accounts = client.get_accounts()
 
   def volume(product_id = "BTC-USD"):
      print("volume")

      client.market_data()

   def get_price(product_id = "BTC-USD"):
      print("get_price")

      # Retrieve current price
      product = client.get_product(product_id)
      current_price = float(product["price"])
      adjusted_price = str(math.floor(current_price - (current_price * 0.05)))

      return current_price
     
      #print("current_price for", product_id, "=", current_price)
      #print("adjusted_price =", adjusted_price)

      #use Ctrl + c to comment a selected block of code.
      # limit_order = client.limit_order_buy(
      #     client_order_id="my_custom_order_id",
      #     product_id=product_id,
      #     price=str(limit_price),
      #     size="0.01"  # Specify the desired size


   def print_accounts():
  #  accounts = client.get_portfolios()
  #  print(dumps(accounts, indent=2))
    for i in accounts["accounts"]:
  #      if i["available_balance"]
        #only print stuff where 'value' != '0'
        print(i["available_balance"] )

   def temp():
    x = client.get_products()
    return x


# Iterating through the json list
#   for i in data:
#      print(i)


except:
   print(">>> Something Broke <<<")
finally:
   file.close()

#END TRY


# coins: AUCTION-USD AVAX-USD BONK-USD CTX-USD MEDIA-USD NCT-USD ORCA-USD PRIME-USD
print( get_price("CTX-USD") )
my_dict = temp()

with open("coinbase_products.txt", "w") as file:
   for key, value in my_dict.items():
      file.write(f"{key}: {value}\n")

"""
{
  "accounts": [
    {
      "uuid": "11e1e473-74a7-5812-90fb-caed1cf44f77",
      "name": "MEDIA Wallet",
      "currency": "MEDIA",
      "available_balance": {
        "value": "11.5",
        "currency": "MEDIA"
      },
      "default": true,
      "active": true,
      "created_at": "2024-02-14T19:27:47.684Z",
      "updated_at": "2024-02-14T21:03:40.388Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "MEDIA"
      }
    },
    {
      "uuid": "ecd8caad-3801-565a-b285-0018a346a37d",
      "name": "ZETA Wallet",
      "currency": "ZETA",
      "available_balance": {
        "value": "0",
        "currency": "ZETA"
      },
      "default": true,
      "active": true,
      "created_at": "2024-02-13T08:15:40.923Z",
      "updated_at": "2024-02-13T08:15:40.923Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ZETA"
      }
    },
    {
      "uuid": "e7c2dc2f-50b3-518b-9d60-b0cf921adfae",
      "name": "ORCA Wallet",
      "currency": "ORCA",
      "available_balance": {
        "value": "0",
        "currency": "ORCA"
      },
      "default": true,
      "active": true,
      "created_at": "2024-01-22T00:50:46.845Z",
      "updated_at": "2024-02-09T17:42:55.126Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ORCA"
      }
    },
    {
      "uuid": "6c7f4bd4-271c-5b0f-ad4d-b022c9fc7bb0",
      "name": "NCT Wallet",
      "currency": "NCT",
      "available_balance": {
        "value": "0",
        "currency": "NCT"
      },
      "default": true,
      "active": true,
      "created_at": "2023-12-20T05:10:24.052Z",
      "updated_at": "2024-02-06T23:53:46.383Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "NCT"
      }
    },
    {
      "uuid": "a6cf86ca-552f-5874-b360-c3e58dba9308",
      "name": "BONK Wallet",
      "currency": "BONK",
      "available_balance": {
        "value": "0",
        "currency": "BONK"
      },
      "default": true,
      "active": true,
      "created_at": "2023-12-15T06:10:43.442Z",
      "updated_at": "2024-02-05T21:24:08.134Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "BONK"
      }
    },
    {
      "uuid": "aea123d0-0c0f-547e-ad2b-39803f08267a",
      "name": "CTX Wallet",
      "currency": "CTX",
      "available_balance": {
        "value": "0",
        "currency": "CTX"
      },
      "default": true,
      "active": true,
      "created_at": "2023-11-19T14:21:42.480Z",
      "updated_at": "2024-02-06T23:53:46.354Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "CTX"
      }
    },
    {
      "uuid": "0eb0b00c-8b5b-5c06-a914-537935b8031f",
      "name": "AVAX Wallet",
      "currency": "AVAX",
      "available_balance": {
        "value": "0.25",
        "currency": "AVAX"
      },
      "default": true,
      "active": true,
      "created_at": "2023-11-18T08:29:30.808Z",
      "updated_at": "2023-12-03T00:00:29.975Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "AVAX"
      }
    },
    {
      "uuid": "370ac40d-6165-5070-a54f-605f83b1665d",
      "name": "UST Wallet",
      "currency": "UST",
      "available_balance": {
        "value": "0",
        "currency": "UST"
      },
      "default": true,
      "active": true,
      "created_at": "2023-11-11T20:35:52.636Z",
      "updated_at": "2023-11-11T20:35:53.179Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "UST"
      }
    },
    {
      "uuid": "9dcfe2fd-4e59-599b-9b44-1569a601288e",
      "name": "AUCTION Wallet",
      "currency": "AUCTION",
      "available_balance": {
        "value": "90",
        "currency": "AUCTION"
      },
      "default": true,
      "active": true,
      "created_at": "2023-11-05T06:49:23.523Z",
      "updated_at": "2024-02-09T19:54:16.602Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "AUCTION"
      }
    },
    {
      "uuid": "880397cd-6532-5b2f-b14a-542b3d5c89b0",
      "name": "PRIME Wallet",
      "currency": "PRIME",
      "available_balance": {
        "value": "120",
        "currency": "PRIME"
      },
      "default": true,
      "active": true,
      "created_at": "2023-11-03T19:13:30.422Z",
      "updated_at": "2024-02-06T23:53:46.320Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "PRIME"
      }
    },
    {
      "uuid": "d2a3021c-e0a5-5abb-82ff-28cae03593e3",
      "name": "ETH2 Wallet",
      "currency": "ETH2",
      "available_balance": {
        "value": "0.01356595025",
        "currency": "ETH2"
      },
      "default": true,
      "active": true,
      "created_at": "2023-07-24T16:09:11.150Z",
      "updated_at": "2024-02-15T21:20:22.312Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": false,
      "hold": {
        "value": "0",
        "currency": "ETH2"
      }
    },
    {
      "uuid": "cd5214e8-bcc7-5a75-8b96-80d48fe0a40d",
      "name": "AST Wallet",
      "currency": "AST",
      "available_balance": {
        "value": "0",
        "currency": "AST"
      },
      "default": true,
      "active": true,
      "created_at": "2022-07-12T12:14:11.465Z",
      "updated_at": "2022-07-12T12:14:11.465Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "AST"
      }
    },
    {
      "uuid": "6b0ff940-cfb3-5df5-beb1-0c5d28d0deb3",
      "name": "FIS Wallet",
      "currency": "FIS",
      "available_balance": {
        "value": "0",
        "currency": "FIS"
      },
      "default": true,
      "active": true,
      "created_at": "2022-06-17T07:04:56.730Z",
      "updated_at": "2022-06-17T07:04:56.730Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "FIS"
      }
    },
    {
      "uuid": "582fad1d-196a-5d1d-9eec-0cedabaee036",
      "name": "POND Wallet",
      "currency": "POND",
      "available_balance": {
        "value": "0",
        "currency": "POND"
      },
      "default": true,
      "active": true,
      "created_at": "2022-06-17T07:04:30.913Z",
      "updated_at": "2022-06-17T07:04:30.913Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "POND"
      }
    },
    {
      "uuid": "02bba143-0cf2-54dc-a0d4-6fbf15c90c1d",
      "name": "SYN Wallet",
      "currency": "SYN",
      "available_balance": {
        "value": "0",
        "currency": "SYN"
      },
      "default": true,
      "active": true,
      "created_at": "2022-05-23T17:13:18.011Z",
      "updated_at": "2022-05-23T17:13:18.011Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "SYN"
      }
    },
    {
      "uuid": "609aab29-1173-56b6-b0cf-c8fedae4d58d",
      "name": "ARPA Wallet",
      "currency": "ARPA",
      "available_balance": {
        "value": "10",
        "currency": "ARPA"
      },
      "default": true,
      "active": true,
      "created_at": "2022-01-02T00:31:22.953Z",
      "updated_at": "2022-11-19T08:41:57.637Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ARPA"
      }
    },
    {
      "uuid": "a793333b-7ba3-5a70-b423-ea05ff69392c",
      "name": "USDC Wallet",
      "currency": "USDC",
      "available_balance": {
        "value": "120.3235814898",
        "currency": "USDC"
      },
      "default": true,
      "active": true,
      "created_at": "2022-01-02T00:31:22.788Z",
      "updated_at": "2024-02-14T21:03:40.243Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "USDC"
      }
    },
    {
      "uuid": "17600ac0-1d37-5bc5-9a73-01c356b2c941",
      "name": "TRU Wallet",
      "currency": "TRU",
      "available_balance": {
        "value": "0",
        "currency": "TRU"
      },
      "default": true,
      "active": true,
      "created_at": "2021-12-19T08:59:56.683Z",
      "updated_at": "2021-12-19T08:59:56.683Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "TRU"
      }
    },
    {
      "uuid": "53c71f13-936b-53b8-b4d3-12d479922491",
      "name": "PERP Wallet",
      "currency": "PERP",
      "available_balance": {
        "value": "0",
        "currency": "PERP"
      },
      "default": true,
      "active": true,
      "created_at": "2021-11-30T15:55:32.704Z",
      "updated_at": "2021-11-30T15:55:32.704Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "PERP"
      }
    },
    {
      "uuid": "3da3e6cb-79bd-5be1-8ab9-f3bd26b44ca5",
      "name": "MANA Wallet",
      "currency": "MANA",
      "available_balance": {
        "value": "9.60194061",
        "currency": "MANA"
      },
      "default": true,
      "active": true,
      "created_at": "2021-11-28T08:30:31.190Z",
      "updated_at": "2022-11-19T08:42:06.295Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "MANA"
      }
    },
    {
      "uuid": "9994629a-a585-5468-8736-ec9d957e826c",
      "name": "XYO Wallet",
      "currency": "XYO",
      "available_balance": {
        "value": "0",
        "currency": "XYO"
      },
      "default": true,
      "active": true,
      "created_at": "2021-11-20T05:50:36.758Z",
      "updated_at": "2021-11-20T05:50:36.758Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "XYO"
      }
    },
    {
      "uuid": "3471943f-a648-5a01-8d2f-9457c111470a",
      "name": "IOTX Wallet",
      "currency": "IOTX",
      "available_balance": {
        "value": "25012.94364852",
        "currency": "IOTX"
      },
      "default": true,
      "active": true,
      "created_at": "2021-11-12T01:05:22.551Z",
      "updated_at": "2024-02-06T23:53:46.151Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "IOTX"
      }
    },
    {
      "uuid": "7bd79b24-1018-5595-9df8-bb6ff5a05fa3",
      "name": "TRAC Wallet",
      "currency": "TRAC",
      "available_balance": {
        "value": "0.02319397",
        "currency": "TRAC"
      },
      "default": true,
      "active": true,
      "created_at": "2021-11-07T19:44:33.219Z",
      "updated_at": "2024-02-05T21:24:07.419Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "TRAC"
      }
    },
    {
      "uuid": "bb14b50d-4044-54a3-879e-6fe059496f0e",
      "name": "MLN Wallet",
      "currency": "MLN",
      "available_balance": {
        "value": "0.00023925",
        "currency": "MLN"
      },
      "default": true,
      "active": true,
      "created_at": "2021-11-06T07:16:57.594Z",
      "updated_at": "2022-11-19T08:42:06.360Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "MLN"
      }
    },
    {
      "uuid": "d06fed3e-c3f9-5e86-9759-3999a8e3524d",
      "name": "1INCH Wallet",
      "currency": "1INCH",
      "available_balance": {
        "value": "18.50480342",
        "currency": "1INCH"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-22T06:24:23.860Z",
      "updated_at": "2021-10-22T06:24:37.875Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "1INCH"
      }
    },
    {
      "uuid": "8f08c455-bc3c-57d7-ad07-4bc42c12ca26",
      "name": "SKL Wallet",
      "currency": "SKL",
      "available_balance": {
        "value": "0",
        "currency": "SKL"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-17T05:32:56.327Z",
      "updated_at": "2022-01-02T00:31:51.732Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "SKL"
      }
    },
    {
      "uuid": "cbc0cb15-01c9-54d0-9525-cbedd2fff9c4",
      "name": "OXT Wallet",
      "currency": "OXT",
      "available_balance": {
        "value": "149.61463261",
        "currency": "OXT"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-17T05:22:44.845Z",
      "updated_at": "2021-10-17T05:23:03.501Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "OXT"
      }
    },
    {
      "uuid": "ebe8157f-74ab-5d45-94d4-109983fde217",
      "name": "JASMY Wallet",
      "currency": "JASMY",
      "available_balance": {
        "value": "0.30844918",
        "currency": "JASMY"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-12T07:31:11.121Z",
      "updated_at": "2023-12-03T00:00:29.682Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "JASMY"
      }
    },
    {
      "uuid": "c131988e-6229-54a4-aec8-02f95dc21217",
      "name": "OGN Wallet",
      "currency": "OGN",
      "available_balance": {
        "value": "61.42706777",
        "currency": "OGN"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-05T06:43:11.201Z",
      "updated_at": "2021-10-05T06:45:31.702Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "OGN"
      }
    },
    {
      "uuid": "82f25b1e-f5d2-5917-8ad5-bc6517634e83",
      "name": "ENJ Wallet",
      "currency": "ENJ",
      "available_balance": {
        "value": "33.23230126",
        "currency": "ENJ"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-04T05:44:36.759Z",
      "updated_at": "2021-10-04T05:47:37.433Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ENJ"
      }
    },
    {
      "uuid": "441b05d5-d542-5475-b7ee-0454c694af9f",
      "name": "RAD Wallet",
      "currency": "RAD",
      "available_balance": {
        "value": "4.24769147",
        "currency": "RAD"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-04T05:32:47.402Z",
      "updated_at": "2021-10-12T07:33:13.052Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "RAD"
      }
    },
    {
      "uuid": "496f1275-5605-5a77-8684-bccee5db12e8",
      "name": "POLY Wallet",
      "currency": "POLY",
      "available_balance": {
        "value": "0",
        "currency": "POLY"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-04T05:25:31.679Z",
      "updated_at": "2021-11-12T01:05:32.253Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "POLY"
      }
    },
    {
      "uuid": "4b1ee5f8-eefc-5b03-a72b-caaca5187880",
      "name": "AXS Wallet",
      "currency": "AXS",
      "available_balance": {
        "value": "0.45371238",
        "currency": "AXS"
      },
      "default": true,
      "active": true,
      "created_at": "2021-10-02T05:13:55.654Z",
      "updated_at": "2021-10-04T05:23:22.905Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "AXS"
      }
    },
    {
      "uuid": "bef31293-96b4-5ad8-a284-e14aa741ec1c",
      "name": "CRV Wallet",
      "currency": "CRV",
      "available_balance": {
        "value": "0",
        "currency": "CRV"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-28T06:03:25.989Z",
      "updated_at": "2021-09-28T06:03:25.989Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "CRV"
      }
    },
    {
      "uuid": "d211375b-183e-5540-be70-2387c07e76ce",
      "name": "COTI Wallet",
      "currency": "COTI",
      "available_balance": {
        "value": "107.73311791",
        "currency": "COTI"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-25T07:40:40.611Z",
      "updated_at": "2021-09-25T07:43:36.243Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "COTI"
      }
    },
    {
      "uuid": "a083f055-6ac8-597d-84d9-2e01718f8835",
      "name": "CGLD Wallet",
      "currency": "CGLD",
      "available_balance": {
        "value": "0",
        "currency": "CGLD"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-20T19:17:56.355Z",
      "updated_at": "2021-11-12T01:08:12.925Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "CGLD"
      }
    },
    {
      "uuid": "4a478f59-723e-58ad-be82-a102a56c74e3",
      "name": "XTZ Wallet",
      "currency": "XTZ",
      "available_balance": {
        "value": "0",
        "currency": "XTZ"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-18T15:44:02.208Z",
      "updated_at": "2023-10-27T20:21:25.799Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "XTZ"
      }
    },
    {
      "uuid": "98a9c105-abee-5fad-9e44-a51ba03b425c",
      "name": "RGT Wallet",
      "currency": "RGT",
      "available_balance": {
        "value": "2.8094009",
        "currency": "RGT"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-18T14:09:14.152Z",
      "updated_at": "2021-09-25T08:06:04.089Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "RGT"
      }
    },
    {
      "uuid": "c65e9e35-a7a2-5d1c-8a50-cad9209bf05c",
      "name": "ANKR Wallet",
      "currency": "ANKR",
      "available_balance": {
        "value": "575.84318859",
        "currency": "ANKR"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-13T07:39:01.243Z",
      "updated_at": "2021-09-24T15:20:14.368Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ANKR"
      }
    },
    {
      "uuid": "d104d262-ad4a-538e-aae3-f6d4f32ae817",
      "name": "REN Wallet",
      "currency": "REN",
      "available_balance": {
        "value": "64.08540051",
        "currency": "REN"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-13T07:38:14.893Z",
      "updated_at": "2021-09-20T19:22:15.617Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "REN"
      }
    },
    {
      "uuid": "a60449a4-54ba-57cb-8bd1-58544e134cdf",
      "name": "XLM Wallet",
      "currency": "XLM",
      "available_balance": {
        "value": "174.0758571",
        "currency": "XLM"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-13T07:37:41.980Z",
      "updated_at": "2021-09-20T19:32:44.359Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "XLM"
      }
    },
    {
      "uuid": "35025faf-5f46-5320-ac71-7c5674706b1d",
      "name": "ALGO Wallet",
      "currency": "ALGO",
      "available_balance": {
        "value": "33.271916",
        "currency": "ALGO"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-08T08:01:22.474Z",
      "updated_at": "2023-04-26T19:07:26.775Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ALGO"
      }
    },
    {
      "uuid": "7a304a18-8554-5cf6-8166-9d279485634c",
      "name": "SUSHI Wallet",
      "currency": "SUSHI",
      "available_balance": {
        "value": "0",
        "currency": "SUSHI"
      },
      "default": true,
      "active": true,
      "created_at": "2021-09-01T05:05:27.960Z",
      "updated_at": "2021-09-01T12:34:16.232Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "SUSHI"
      }
    },
    {
      "uuid": "f989b201-3dc4-5bcc-81b9-a829d4d52812",
      "name": "ATOM Wallet",
      "currency": "ATOM",
      "available_balance": {
        "value": "0",
        "currency": "ATOM"
      },
      "default": true,
      "active": true,
      "created_at": "2021-08-27T12:42:35.372Z",
      "updated_at": "2023-10-27T20:15:08.410Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ATOM"
      }
    },
    {
      "uuid": "e2c14747-b253-5052-9038-fc65426d1033",
      "name": "ADA Wallet",
      "currency": "ADA",
      "available_balance": {
        "value": "0",
        "currency": "ADA"
      },
      "default": true,
      "active": true,
      "created_at": "2021-08-27T12:40:47.189Z",
      "updated_at": "2021-11-12T01:06:04.096Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "ADA"
      }
    },
    {
      "uuid": "486d0e91-6f3a-536f-8dfd-f75b459c9a76",
      "name": "SHIB Wallet",
      "currency": "SHIB",
      "available_balance": {
        "value": "0.61535689",
        "currency": "SHIB"
      },
      "default": true,
      "active": true,
      "created_at": "2021-08-26T06:58:28.029Z",
      "updated_at": "2023-12-03T00:00:29.373Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "SHIB"
      }
    },
    {
      "uuid": "2b2f1d61-9ff7-53af-87c1-6a8fcce9cec1",
      "name": "TRIBE Wallet",
      "currency": "TRIBE",
      "available_balance": {
        "value": "113.34605218",
        "currency": "TRIBE"
      },
      "default": true,
      "active": true,
      "created_at": "2021-08-24T04:54:27.734Z",
      "updated_at": "2021-11-12T23:51:46.167Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "TRIBE"
      }
    },
    {
      "uuid": "889419dd-55d2-5d31-9bbb-971a7f2998fa",
      "name": "SOL Wallet",
      "currency": "SOL",
      "available_balance": {
        "value": "0.119416762",
        "currency": "SOL"
      },
      "default": true,
      "active": true,
      "created_at": "2021-08-23T22:25:13.500Z",
      "updated_at": "2024-02-05T21:24:07.342Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "SOL"
      }
    },
    {
      "uuid": "6cf8db83-f425-568b-9977-0e5bc9b757bf",
      "name": "XRP Wallet",
      "currency": "XRP",
      "available_balance": {
        "value": "0",
        "currency": "XRP"
      },
      "default": true,
      "active": true,
      "created_at": "2021-08-22T14:21:11.321Z",
      "updated_at": "2021-08-22T14:21:11.321Z",
      "deleted_at": null,
      "type": "ACCOUNT_TYPE_CRYPTO",
      "ready": true,
      "hold": {
        "value": "0",
        "currency": "XRP"
      }
    }
  ],
  "has_next": true,
  "cursor": "aee4ea20-e316-55ec-9d02-43592915332e",
  "size": 49
}
"""
