print("Welcome to Retail Sales Analytics Project!")
import numpy as np
import pandas as pd
df=pd.read_csv("Data/train.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
df['Order Date']=pd.to_datetime(df['Order Date'],errors='coerce')
print(df['Order Date'].dtype)
df['Year']=df['Order Date'].dt.year
df['Month']=df['Order Date'].dt.month
df['Quarter']="Q" + df['Order Date'].dt.quarter.astype(str)
print(df[['Order Date','Year','Month','Quarter']].head(20))
df.to_csv("Data/sales_cleaned.csv", index=False)
print(df.nunique())
print(df['Region'].value_counts())
print(df['Category'].value_counts())
print(df['Sub-Category'].value_counts()) 
   