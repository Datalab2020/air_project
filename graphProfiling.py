#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:11:13 2020

@author: formateur
"""

import pandas as pd
import plotly.graph_objects as go
import numpy as np
import pandas_profiling

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

df["jour"] = pd.DatetimeIndex(df["date_ech"]).day
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["an"] = pd.DatetimeIndex(df["date_ech"]).year
df["axe"] = df["an"].astype(str) + df["mois"].astype(str)
df["axeTemp"] = df["axe"].astype(int)
dfGroup = df.groupby(['X','Y','lib_zone','mois','an', 'date_ech'])

dfAgre = dfGroup.agg({"val_no2" : 'mean',
                       "val_so2" : 'mean',
                       "val_o3" : 'mean',
                       "val_pm25" : 'mean',
                       "val_pm10" : 'mean'})


dfAgre_index = dfAgre.reset_index()

#avec cette ligne je crée une variable avec le df de chaque ville  
for ville in dfAgre_index['lib_zone']:
        globals()['Ville_%s' % ville] = dfAgre_index.loc[:, ][dfAgre_index.lib_zone == ville].sort_values(by=['date_ech']).reset_index()

"""
profile = pandas_profiling.ProfileReport(Ville_TOURS)
profile.to_file("Tours.html")

profile = pandas_profiling.ProfileReport(Ville_BLOIS)
profile.to_file("Blois.html")

profile = pandas_profiling.ProfileReport(Ville_MONTARGIS)
profile.to_file("Montargis.html")
"""
profile = pandas_profiling.ProfileReport(Ville_DREUX)
profile.to_file("Dreux.html")

profile = pandas_profiling.ProfileReport(Ville_CHARTRES)
profile.to_file("Chartres.html")

profile = pandas_profiling.ProfileReport(Ville_ORLEANS)
profile.to_file("Orleans.html")

profile = pandas_profiling.ProfileReport(Ville_CHATEAUROUX)
profile.to_file("Chateauroux.html")

profile = pandas_profiling.ProfileReport(Ville_BOURGES)
profile.to_file("Bourges.html")

anBlois = Ville_BLOIS.describe(include='all')

anMonta = Ville_MONTARGIS.describe(include='all')