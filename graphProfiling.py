#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:11:13 2020

@author: formateur
"""

import pandas as pd


url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

df["jour"] = pd.DatetimeIndex(df["date_ech"]).day
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["an"] = pd.DatetimeIndex(df["date_ech"]).year
"""concat an/mois
df["axe"] = df["an"].astype(str) + df["mois"].astype(str)
df["axeTemp"] = df["axe"].astype(int)
"""
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

# Essai 1 fonction sous alias
def moy(ville):
    return df.loc[(df["lib_zone"] == ville)].groupby(["an", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm25", "val_pm10"]]

moyBlo = moy("BLOIS")
moyBou = moy("BOURGES")
moyChar = moy("CHARTRES")
moyChat = moy("CHATEAUROUX")
moyDre = moy("DREUX")
moyMon = moy("MONTARGIS")
moyOrl = moy("ORLEANS")
moyTou = moy("TOURS")


""" créa fic html
profile = pandas_profiling.ProfileReport(Ville_TOURS)
profile.to_file("Tours.html")

profile = pandas_profiling.ProfileReport(Ville_BLOIS)
profile.to_file("Blois.html")

profile = pandas_profiling.ProfileReport(Ville_MONTARGIS)
profile.to_file("Montargis.html")

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
"""
""" sunburst
data = dict(
    origine=["Tours", "2018", "2019", "2020", "no2", "so2", "o3", "pm10"],
    parent=["", "Tours", "Tours", "Tours", "2018", "2018", "2018", "2018" ],
    value=[0, 0, 0, 0, 1.578, 1, 3.715, 2.865])

fig = px.sunburst(
    data,
    names='originer',
    parents='parent',
    values='value',
)
fig.show()
"""

#print(moyTou.describe())
"""
dfQual = df.loc[:, ["qualif", "lib_zone"]].groupby(["lib_zone", "qualif"])

print(dfQual.size())
print(dfQual.size().reset_index())
"""
"""
dfVal = df.loc[:, ["valeur", "lib_zone"]].groupby(["lib_zone", "valeur"])

new = dfVal.size().reset_index().sort_values(by= ["lib_zone", "valeur"])
"""
