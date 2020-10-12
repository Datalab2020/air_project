#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:52:13 2020

@author: formateur
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas_profiling


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

#avec cette ligne je crée une variable avec le df de chaque ville  
for ville in aggregation_index['lib_zone']:
        globals()['Ville_%s' % ville] = aggregation_index.loc[:, ][aggregation_index.lib_zone == ville].sort_values(by=['date_ech']).reset_index()


profile = pandas_profiling.ProfileReport(Ville_TOURS)
profile.to_file("Tours.html")
