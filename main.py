# here is where you put the backtest code and data
import numpy as np
import pandas as pd
import seaborn as sns

df_1 = pd.read_csv('C:/DS 303/Project/Portfolio Optimization/HISTORICAL_DATA/HISTORICAL_DATA/BHEL_data.csv')
df_2 = pd.read_csv('C:/DS 303/Project/Portfolio Optimization/HISTORICAL_DATA/HISTORICAL_DATA/BOMDYEING_data.csv')
df_3 = pd.read_csv('C:/DS 303/Project/Portfolio Optimization/HISTORICAL_DATA/HISTORICAL_DATA/BPCL_data.csv')
df_4 = pd.read_csv('C:/DS 303/Project/Portfolio Optimization/HISTORICAL_DATA/HISTORICAL_DATA/BRITANNIA_data.csv')
data = [df_1['close'], df_2['close'], df_3['close'], df_4['close']]

# to create a model, do: model = Model(), 
model = Model()

# to get the optimized portfolio coefficients, do: coeffs = model.fit(df), where df is a DataFrame of closing prices of various assets
coeffs = model.fit(df)
# an example can be found here: https://www.quantconnect.com/terminal/processCache/?request=embedded_backtest_4ebbe01bfea8c5ae6f98fcda38a50b1c.html
