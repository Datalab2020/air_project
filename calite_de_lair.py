#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:04:47 2020

@author: formateur
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)


df["jour"] = pd.DatetimeIndex(df["date_ech"]).day
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["an"] = pd.DatetimeIndex(df["date_ech"]).year

#print(df.head())
#info=df.info()

group_villes2 = df.groupby(['X','Y','lib_zone','mois','an','date_ech','valeur'])

aggregation = group_villes2.agg({'val_no2' : 'mean',
                                 'val_so2' : 'mean',
                                 'val_o3' : 'mean',
                                 'val_pm10' : 'mean',
                                 'val_pm25' : 'mean'})

aggregation_index = aggregation.reset_index().sort_values(by=['date_ech','lib_zone'])

plt.figure(figsize=(20, 16))
sns.relplot(x="date_ech", y="valeur", kind="line", hue="lib_zone", col="lib_zone", col_wrap=3,
            data=aggregation_index.query("date_ech >= '2018/07/01 00:00:00+00' & date_ech < '2019/01/01 00:00:00+00'"))


"""
#avec cette ligne je crée une variable avec le df de chaque ville  
for ville in aggregation_index['lib_zone']:
        globals()['Ville_%s' % ville] = aggregation_index.loc[:, ][aggregation_index.lib_zone == ville].sort_values(by=['date_ech']).reset_index()

#print(Ville_BLOIS)


Bl = aggregation_index.loc[:, ][aggregation_index.lib_zone == 'BLOIS'][aggregation_index.an > 2018].sort_values(by=['an', 'mois']).reset_index()
#Bl[['val_no2','val_so2','val_o3','val_pm10']].plot.hist(alpha=0.3)
#Bl[['val_no2','val_so2','val_o3','val_pm10']].plot.kde()
"""   
        

