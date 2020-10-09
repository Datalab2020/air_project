import pandas as pd

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)
#print(df)

print(df.head())

print(df.index)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.size)
print(df.shape)
print(df.isna().sum())
print(df.describe(include="all"))

print(df.loc[0])
print(df.loc[:, ["X", "Y", "date_ech"]])

print(df.isin({"X": [1.903984]}))
print(df.agg("mean"))
print(df.agg(["min", "mean", "max"]))

print(df.plot.scatter(x="X", y="Y", c="orange"))
print(df.index)
print(df.plot.scatter(x= "date_ech", y= "val_so2", c="orange"))
