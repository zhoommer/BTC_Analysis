from pandas_ods_reader import read_ods
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "/home/mrrobot/Documents/Crypto&Bist/BTC_Analysis/BTC_Data.ods"

# load a sheet based on its index (1 based)
sheet_idx = 1
df = read_ods(path, sheet_idx)
# Create BTC DataFrame
df_BtcData = pd.DataFrame(df)

close = df_BtcData[df_BtcData['Close**'] == 60000][['Date', 'Close**']]


# Bitcoin son 7 gunluk kapanis ortalamasi
print('ACILIS & KAPANIS ORTALAMALARI')
last_seven_close = df_BtcData['Close**'].tail(7).mean()
print(f'Son 7 gunluk kapanis ortalamasi = {last_seven_close}')

# Bitcoin son 7 gunluk acilis ortalamasi

last_seven_open = df_BtcData['Open*'].tail(7).mean()
print(f'Son 7 gunluk acilis ortalamasi = {last_seven_open}')

print('---------------------------------------------------------')

# Bitcoin Son 25 gunluk kapanis ortalamasi
last_twentyfive_close = df_BtcData['Close**'].tail(25).mean()
print(f'Son 25 gunluk kapanis ortalamasi = {last_twentyfive_close}')

# Bitcoin Son 25 gunluk acilis ortalamasi
last_twentyfive_open = df_BtcData['Open*'].tail(25).mean()
print(f'Son 25 gunluk acilis ortalamasi = {last_twentyfive_open}')

print('---------------------------------------------------------')

# Bitcoin Son 99 gunluk kapanis ortalamasi
last_ninety_close = df_BtcData['Close**'].tail(99).mean()
print(f'Son 99 gunluk kapanis ortalamasi = {last_ninety_close}')

# Bitcoin Son 99 gunluk acilis ortalamasi
last_ninety_open = df_BtcData['Open*'].tail(99).mean()
print(f'Son 99 gunluk acilis ortalamasi = {last_ninety_open}')

print('---------------------------------------------------------')
print('EN DUSUK & EN YUKSEK DEGER ORTALAMALARI')

# Bitcoin Son 7 gunluk en dusuk deger ortalamasi
last_seven_low = df_BtcData['Low'].tail(7).mean()
print(f'Son 7 gunluk en dusuk deger ortalamasi = { last_seven_low }')

# Bitcoin Son 7 gunluk en yuksek deger ortalamasi
last_seven_high = df_BtcData['High'].tail(7).mean()
print(f'Son 7 gunluk en yuksek deger ortalamasi = { last_seven_high }')

print('---------------------------------------------------------')

# Bitcoin Son 25 gunluk en dusuk deger ortalamasi
last_twentyfive_low = df_BtcData['Low'].tail(25).mean()
print(f'Son 25 gunluk en dusuk deger ortalamasi = { last_twentyfive_low }')

# Bitcoin Son 25 gunluk en yuksek deger ortalamasi
last_twentyfive_high = df_BtcData['High'].tail(25).mean()
print(f'Son 25 gunluk en yuksek deger ortalamasi = { last_twentyfive_high }')

print('---------------------------------------------------------')

# Bitcoin Son 99 gunluk en dusuk deger ortalamasi
last_ninety_low = df_BtcData['Low'].tail(99).mean()
print(f'Son 99 gunluk en dusuk ortalamasi = {last_ninety_low}')

# Bitcoin Son 99 gunluk acilis ortalamasi
last_ninety_high = df_BtcData['High'].tail(99).mean()
print(f'Son 99 gunluk en yuksek ortalamasi = {last_ninety_high}')
