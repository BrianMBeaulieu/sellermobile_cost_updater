import pandas as pd
import sys
import os

print(len(sys.argv))
if len(sys.argv) < 2:
    print("Usage: ")
    sys.exit(1)

file = sys.argv[1]

data = pd.read_excel(file,sheet_name='Items')

df = pd.DataFrame(data)
skus = df['sku']
cogs = df['cogs']
asins = df['asin']
cogs_update_past_orders = df['cogs_update_past_orders']

for i in range(0,len(df)):
    sku = skus[i]
    if "_" in str(sku):
        cost = round(float(sku.split('_')[1]),2)
        cog = round(cogs[i],2)
        if str(cog) == "nan":
            cog = 0.00
        asin = asins[i]
        if str(cog) != str(cost) and cog == 0:
            print("Updating %s cost %s => %s" %(asin,cog,cost))
            cogs_update = cogs_update_past_orders[i]
            df.at[i,'cogs_update_past_orders'] = 'Yes'
            df.at[i,'cogs'] = cost

df.to_excel(excel_writer=file+"_processed.xlsx",sheet_name='Items',index=False)

