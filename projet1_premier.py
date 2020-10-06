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

print(df.loc[0:50, ["Y", "X", "valeur", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"])
df['val_no2'].plot.box()