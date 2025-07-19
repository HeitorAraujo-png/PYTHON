import pandas as pd

tbl = pd.read_csv('weather_data.csv')
tl = tbl['temp'].to_list()

print(f'{tbl['temp'].max():}')