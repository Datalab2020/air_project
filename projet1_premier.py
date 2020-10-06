import datetime
import pandas as pd

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

#print(df.columns)
#print(df.loc[0:50, ["Y", "X", "valeur", "date_ech", "lib_zone"]].sort_values(by= ["lib_zone", "date_ech"], na_position= "last"))
#print(df.groupby("lib_zone").mean().loc[:, ["valeur"]])
#print(df.groupby("lib_zone").mean().reset_index().loc[:, ["valeur", "lib_zone"]])
#print(df.loc[0:50, ["Y", "X", "valeur", "date_ech", "lib_zone"]].df[df["lib_zone"]=="BLOIS"])
#print(df[df["lib_zone"]=="BLOIS"])

var=df.loc[:, ["Y", "X", "val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2019/01/01 00:00:00+00"][df.date_ech < "2019/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

print(var)