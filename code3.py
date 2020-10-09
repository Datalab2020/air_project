import pandas as pd
import datetime

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

#print(df.plot.scatter(x= "date_ech", y= "val_so2", c="orange"))

#print(df.columns)
#print(df.describe())
#print(df.isin({"lib_zone": ["TOURS"]}))
#print(df[df["lib_zone"]== "TOURS"])
#.sort_values(by= ["date_ech"]).df[df["lib_zone"]=="BLOIS"])

#print(df.loc[0:50, "date_ech", "lib_zone"] 

#print(df.loc[0:20, ["date_ech", "lib_zone"]])
#print(df[df['lib_zone'] == "TOURS"].head())
#print(df.sort_values(by=['date_ech']))


#print(df.groupby("lib_zone").max).df.loc[:, ["valeur", "lib_zone"]]
#print(df.columns == ['valeur'.join(x) for x in df.columns.values])
#print((df['lib_zone'].argsort()))
#print(df.loc[df['lib_zone']=="TOURS",:])
#print(df.loc[df['lib_zone'].isin(['TOURS']),:])

#print(df[(df['lib_zone'] == "TOURS") & (df["valeur"])])

colonnes = "lib_zone", "valeur", "qualif"
#print(df.loc[(df['lib_zone'] == "TOURS"), colonnes])

print(df.loc[(df["lib_zone"] == "TOURS"), colonnes].sort_values(by=["valeur"]))

chimie =  "lib_zone", "date_ech", "val_no2", "val_so2", "val_o3", "val_pm10"

print(df.loc[(df["lib_zone"] == "TOURS"), chimie].sort_values(by=["date_ech"]))

print(df.groupby(["lib_zone"]).mean()["val_no2"])
print(df.groupby(["lib_zone"]).mean()["val_so2"])
print(df.groupby(["lib_zone"]).mean()["val_o3"])
print(df.groupby(["lib_zone"]).mean()["val_pm10"])


#df['date_ech'] = pd.to_datetime(df['date_ech'], format="%Y/%d/%m %H:%M")

#df = df.sort_values(by='date_ech', ascending=False)
#print(df.to_csv(index=False))

#df['year'] = df['date_ech'].dt.strftime('%Y')
#df['month'] = df['date_ech'].dt.strftime('%m')

print(df)




