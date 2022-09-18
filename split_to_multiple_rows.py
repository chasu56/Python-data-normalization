# demo for csv brusting


import pandas as pd

df = pd.read_csv('./SalesSample.csv')

df = df.astype(str)

for itm in df.head():
    df[itm] = df[itm].str.split("~")

df = df.apply(pd.Series.explode)

df = df.sort_values(by=["Product code", "Sales"])

df["Sales"] = pd.to_numeric(df["Sales"])
# Pivot by group by

df2 = df.groupby('Product code')["Sales"].sum()

df2.to_csv("./SalesSample_pivoted.csv")

print(df)
