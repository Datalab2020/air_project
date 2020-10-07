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


print("jour")
'''
var = df.loc[:, ["val_no2", "date_ech", "lib_zone"]][df.lib_zone == "BLOIS"][df.date_ech >= "2018/01/01 00:00:00+00"][df.date_ech < "2018/02/01 00:00:00+00"].sort_values(by= ["date_ech"])

test = df.loc(:,["val_no2","val_so2","val_o3","val_pm25","val_pm10","date_ech",[df.lib_zone == "BLOIS"]]).groupby(["BLOIS"]).mean()

print(test)

var = df.loc[:, ["date_ech"]]
'''