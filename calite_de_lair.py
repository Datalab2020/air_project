#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:04:47 2020

@author: formateur
"""

import pandas as pd


url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)


df["jour"] = pd.DatetimeIndex(df["date_ech"]).day
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["an"] = pd.DatetimeIndex(df["date_ech"]).year

#print(df.head())
info=df.info()

group_villes = df.groupby(['lib_zone'])
group_villes2 = df.groupby(['X','Y','lib_zone','mois','an'])

aggregation = group_villes2.agg({'val_no2' : 'mean',
                                 'val_so2' : 'mean',
                                 'val_o3' : 'mean',
                                 'val_pm10' : 'mean',
                                 'val_pm25' : 'mean'})

aggregation_index = aggregation.reset_index()



   
for ville in aggregation_index['lib_zone']:
        globals()['Ville_%s' % ville] = aggregation_index.loc[:, ][aggregation_index.lib_zone == ville].sort_values(by=['an', 'mois']).reset_index()
       # globals()['Ville_%s' % ville][['val_no2','val_so2','val_o3','val_pm10']].plot.kde()   



Bl = aggregation_index.loc[:, ][aggregation_index.lib_zone == 'BLOIS'][aggregation_index.an > 2018].sort_values(by=['an', 'mois']).reset_index()
print(Bl)
Bl[['val_no2','val_so2','val_o3','val_pm10']].plot.hist(alpha=0.3)
Bl[['val_no2','val_so2','val_o3','val_pm10']].plot.kde()
Bl.plot.scatter(x='val_no2', y='val_so2', c='Orange')       
        

