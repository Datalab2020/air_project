import datetime
import pandas as pd

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

#print(df.isna().sum())
#print(df.columns)
#print(df.loc[0:50, ["Y", "X", "valeur", "date_ech", "lib_zone"]].sort_values(by= ["lib_zone", "date_ech"], na_position= "last"))
#print(df.groupby("lib_zone").mean().loc[:, ["valeur"]])
#print(df.groupby("lib_zone").mean().reset_index().loc[:, ["valeur", "lib_zone"]])
#print(df.loc[0:50, ["Y", "X", "valeur", "date_ech", "lib_zone"]].df[df["lib_zone"]=="BLOIS"])
#print(df[df["lib_zone"]=="BLOIS"])

'''
Idée en stand-by, trop laborieux !!!!!

#Polluant Blois 2018
#Janvier
2018janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
2018janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Février
fevBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/02/01 00:00:00+00"][df.date_ech < "2018/03/01 00:00:00+00"].sort_values(by= ["date_ech"])
fevBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/02/01 00:00:00+00"][df.date_ech < "2018/03/01 00:00:00+00"].sort_values(by= ["date_ech"])
fevBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/02/01 00:00:00+00"][df.date_ech < "2018/03/01 00:00:00+00"].sort_values(by= ["date_ech"])
fevBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/02/01 00:00:00+00"][df.date_ech < "2018/03/01 00:00:00+00"].sort_values(by= ["date_ech"])
fevBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/02/01 00:00:00+00"][df.date_ech < "2018/03/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Mars
marBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/03/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
marBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/03/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
marBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/03/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
marBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/03/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
marBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/03/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Avril
avrBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
avrBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
avrBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
avrBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
avrBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Mai
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Juin
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Juillet
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Aout
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Septembre
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Octobre
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Novembre
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

#Decembre
janBlois_no2=df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_so2=df.loc[:, ["val_so2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBlois_o3=df.loc[:, ["val_o3", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm10=df.loc[:, ["val_pm10", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
janBloispm25=df.loc[:, ["val_pm25", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])


# Moyenne du no2 sur Blois en janvier 2018
print(janBlois_no2)
print(janBlois_no2.agg('mean'))

# Moyenne du no2 sur Blois en janvier 2018
print(janBlois_so2)
print(janBlois_so2.agg('mean'))

# Moyenne du no2 sur Blois en janvier 2018
print(janBlois_o3)
print(janBlois_o3.agg('mean'))

# Moyenne du no2 sur Blois en janvier 2018
print(janBloispm25)
print(janBloispm25.agg('mean'))

# Moyenne du no2 sur Blois en janvier 2018
print(janBloispm10)
print(janBloispm10.agg('mean'))

# Statistiques complètes par polluant sur le mois de janvier 2018
print(janBlois_no2.describe())
print(janBlois_so2.describe())
print(janBlois_o3.describe())
print(janBloispm25.describe())
print(janBloispm10.describe())

'''
var = df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

test = df.loc[:,["val_so2","val_o3","val_pm25","val_pm10","date_ech","lib_zone"]].groupby([df.lib_zone == "BLOIS"]).mean()

print(test)