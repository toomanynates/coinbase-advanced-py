
from coinbase.rest import RESTClient
import json
from json import dumps
from os import listdir
from os.path import isfile, join
import math
import pandas as pd
import time
import datetime

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
   file = open("Enter your C:/Users/ coinbase_cloud_api_key.json filepath here", "r")
#   print(file.read())
   data = json.load(file)

   print(data["name"])
   print(data["privateKey"])

   api_key = data["name"]
   api_secret = data["privateKey"]
   
   client = RESTClient(api_key=api_key, api_secret=api_secret)
   accounts = client.get_accounts()
 
   def get_client():
      return client
       
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
           #if i["available_balance"]
           #only print stuff where 'value' != '0'
           print(i["available_balance"] )

   # Get products from client, then filter to only USDC pairs, then add to Pandas
   def get_products_df(filter='USDC', bOrder=True):
       prods = get_client().get_products()
       prod_list = prods['products']
       #print( len(prod_list) )
       
       # Filter the list so it only includes USDC pairs
       filt_list = [x for x in prod_list if x['product_id'].find(filter) >= 0]
       # presort the list because pandas sort has problems.
       sort_list = sorted(filt_list, key=lambda d: d['product_id'])

       #print( sort_list )     

       # order the list alphabetically
       # 4/15/2024 this is necessary to avoid bugs. get_products() does not always return the products in the same order. Consequently, I must order them to avoid price discrepancies when iteratively adding prices on to the end of the list
       # However, sorting with pandas produces bugs:
           # kind {‘quicksort’ 15 errors, ‘mergesort’ 10 errors, ‘heapsort’ 3 errors, ‘stable’ 3 errors}, default ‘quicksort’
       """
       if bOrder:
          df.sort_values('product_id', inplace=True, kind='stable')
          #kind {‘quicksort’ 15 errors, ‘mergesort’ 10 errors, ‘heapsort’ 3 errors, ‘stable’ 3 errors}, default ‘quicksort’
          #doesn't make a difference if I do it inplace or not
          #it's worse if I sort it twice
          # >>> possible workaround: loop through each row. match the product_id and then assign the 
          # >>> possible workaround: compare the names of the 
          print('get_products_df(): ordering df')
       """
       
       return pd.DataFrame(sort_list)

   def format_filtered_df(df):
       #remove unwanted columns
       dropcols = [5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30, 31, 32, 33, 34]
       dropcols = dropcols[::-1] # Reverse the list. Otherwise it pops them off then shifts the remaining columns down.
        
       for n in dropcols:
           df.drop(df.columns[n], axis=1, inplace=True)   
        
       # return the rearrange columns
       return df[['product_id', 'base_name', 'base_currency_id', 'volume_24h', 'volume_percentage_change_24h', 'price', 'price_percentage_change_24h']]


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
# test the get_price() function
print( get_price("CTX-USD") )

# Write the contends of a dictionary to a file. Useful if the dictionary is too big to view
def dict_to_file(dict, filename="coinbase_products.txt"):
   with open(filename, "w") as file:
      for key, value in dict.items():
         file.write(f"{key}: {value}\n")
         #"C:\Users\tooma\OneDrive\Documents\GitHub\coinbase-advanced-py\coinbase_products.txt"

# END BLOCK 1

# computer the percentage difference between two numbers
def perc_diff(num1, num2):
    if num1 == num2:
        return 0  # The numbers are the same, so the percentage difference is 0.

    # Calculate the percentage difference using the formula
    # use a lambda in case I need to use it quickly elsewhere
    percentage_diff = (lambda num1,num2:(num2 - num1) / ((num2 + num1) / 2) * 100)(num1, num2)
    return percentage_diff

# Iterative cycle that periodically gets a new 'price_percentage_change_24h' and adds it to df
def cycle_prod_updates(df, iterations=1, sleep=300):
    count = 0
    while count < iterations:
        print(f"cycle_prod_updates Iteration {count} of {iterations}")
        time.sleep(sleep)

        #local variables
        dt = datetime.datetime.now()
        str_date = f'{dt.strftime("%Y%m%d %H:%M")}'
        col_name = f'perc_change_{str_date}' # base the column name off the current datetime
        price_name = 'price' # changed from 'price_percentage_change_24h'

       # 1) get new data
        new_df = get_products_df() # get a new filtered list

        # 2) assign new price to the end of the original df
        df[f'{price_name}_{str_date}'] = new_df[price_name]
        
        # 3) make a temp df that contains the new data and the last price from the original
        temp_df = pd.DataFrame()
        temp_df['price1'] = pd.to_numeric(df.iloc[:, -3], errors='raise') # get the last price, convert to numeric
        temp_df['price2'] = pd.to_numeric(df.iloc[:, -1], errors='raise') # get the new price, convert to numeric 
        
        # 4) assign new col to the original df: compute the pct_change() between the cols of the temp df        
        df[col_name] = temp_df.pct_change(axis=1)['price2'].round(4) * 100

        # Find the row that contains the lowest value
        df_min = df[df[col_name] == df[col_name].min()]
        print(f"Lowest price: {df[col_name].min()}")
        print("Row df of lowest price:\n")
        print(df_min)
        
        # Find the row that contains the highest value
        df_max = df[df[col_name] == df[col_name].max()]
        print(f"Largest price: {df[col_name].max()}")
        print("Row df of highest price:\n")
        print(df_max)
        
        df.head(5) # output df info

        df.to_csv(f'coinbase-usdc-{dt.strftime("%Y%m%d")}-0{count}.csv', index=False)

        count += 1 # increment the count
        
    return df

# Iterative cycle that periodically gets a new 'price_percentage_change_24h' and adds it to df
def cycle_prod_updates_temp(df, iterations=1, sleep=300):
    count = 0
    while count < iterations:
        print(f"cycle_prod_updates_temp Iteration {iterations}")
        time.sleep(sleep)

        #local variables
        dt = datetime.datetime.now()
        str_date = f'{dt.strftime("%Y%m%d %H:%M")}'

        # 1) get new data
        new_df = get_products_df() # get a new list, filtered by USDC and ordered alphabetically

        # 2) assign new price to the end of the original df
        df[f'{count} product_id'] = new_df['product_id']
        df[f'price_{str_date}'] = new_df['price']
             
        df.head(5) # output df info

        df.to_csv(f'coinbase-usdc-{dt.strftime("%Y%m%d")}-0{count}.csv', index=False)

        count += 1 # increment the count
        
    return df

# Get products from client, then filter to only USDC pairs, then add to Pandas
df = get_products_df()
# Alternatively, read pandas from CSV
#df = pd.read_csv("coinbase-usdc-unfiltered-pairs-20240403-05.csv")
#df.head()

# Format the dataframe to remove unwanted columns and rearrange them
df = format_filtered_df(df)

# Cycle for a few minutes and build a df with iterative price changes.
df = cycle_prod_updates(df, 24, 3600)
#df = cycle_prod_updates_temp(df, 1, 10)

# Export to CSV
#df.to_csv("coinbase-usdc-unfiltered-pairs.csv", index=False)
print("done")
# Saved to C:\Users\tooma\OneDrive\Documents\GitHub\coinbase-advanced-py\

