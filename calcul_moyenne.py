#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:31:02 2020

@author: formateur
"""

import datetime
import pandas as pd
import folium

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)


df["jour"] = pd.DatetimeIndex(df["date_ech"]).day
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["an"] = pd.DatetimeIndex(df["date_ech"]).year

'''
#var = df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])
#justeBLois = df.groupby([df.lib_zone=="BLOIS"]).mean().reset_index().loc[:,["val_no2","val_so2","val_o3","val_pm25","val_pm10","lib_zone"]]
#test1 = df.groupby("lib_zone").mean().reset_index().loc[:,["val_no2","val_so2","val_o3","val_pm25","val_pm10","lib_zone"]]
'''
#Groupement des villes par mois et années avec moyenne, min et max de chaque polluant
dfGroup = df.groupby(["lib_zone", "mois", "an"])
dfAgre = dfGroup.agg({"val_no2" : ['mean','min','max'],
                       "val_so2" : ['mean','min','max'],
                       "val_o3" : ['mean','min','max'],
                       "val_pm25" : ['mean','min','max'],
                       "val_pm10" : ['mean','min','max']})
print(dfAgre)


