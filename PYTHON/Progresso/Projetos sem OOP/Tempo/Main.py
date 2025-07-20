import pandas as pd

tbl = pd.read_csv('weather_data.csv')
Mo = tbl[tbl.day == 'Monday']
print(Mo)
print((Mo.temp * 9/5) + 32)