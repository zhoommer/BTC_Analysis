from pandas_ods_reader import read_ods
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/home/mrrobot/Documents/Crypto/BTC_Analysis/BTC_Data.ods'
sheet_idx = 1

data = read_ods(path, sheet_idx)
df = pd.DataFrame(data)

ort = df[(df['Date'] >= '01-01-2018') & (df['Date'] <= '12-31-2021')]
print(ort)
