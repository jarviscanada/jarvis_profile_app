import yaml
import pprint
import gspread

gc = gspread.service_account()
#
demo_id="1VznErP1Uezf-L_yBpeFWqFhV07k_wUGAWdt3JW-TCI4"
sh = gc.open_by_key(demo_id)
ws = sh.worksheet("Employees")

print(ws.get_all_values()[1:])
import pandas as pd
df = pd.DataFrame.from_records(ws.get_all_values()[1:], columns=ws.get_all_records()[0])

short_df = df.iloc[1:5]
print(short_df)

#print(gspread_pandas.conf.get_config)
#from gspread_pandas import Spread, Client
#spread = Spread(demo_id)

ws.clear()
ws.update([short_df.columns.values.tolist()]+ short_df.values.tolist())



exit



