#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:30:04 2020

@author: formateur
"""
# importation librairies
import pandas as pd
from datetime import datetime
import folium
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import plotly.express as px

# Dataframe
url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

# indexation par mois et années
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["annee"] = pd.DatetimeIndex(df["date_ech"]).year

# Valeurs max et qualif pour Tours
#colonnes = "lib_zone", "valeur", "qualif"
#print(df.loc[(df["lib_zone"] == "TOURS"), colonnes].sort_values(by=["valeur"]))

# Valeurs polluants pour Tours dans le temps croissant
#tours =  "lib_zone", "date_ech", "val_no2", "val_so2", "val_o3", "val_pm10"
#print(df.loc[(df["lib_zone"] == "TOURS"), tours].sort_values(by=["date_ech"]))

# Moyennes de chaque polluants pour Tours
#print(df.groupby(["lib_zone"]).mean()["val_no2"])
#print(df.groupby(["lib_zone"]).mean()["val_so2"])
#print(df.groupby(["lib_zone"]).mean()["val_o3"])
#print(df.groupby(["lib_zone"]).mean()["val_pm10"])

# Moyennes par années et par mois pour chaque polluants indépendants pour Tours
#ntours= df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_no2"]
#print(df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_so2"])
#print(df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_o3"])
#print(df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_pm10"])

# Moyennes par années et par mois pour les polluants pour Tours
moyenneT = df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10"]]
#print(moyenneT)

# Moyennes par années et par mois pour les polluants pour Bourges
moyenneB = df.loc[(df["lib_zone"] == "BOURGES")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10"]]
#print(moyenneB)

# PLOT
#df.plot.scatter(x='mois',y='val_no2')
#print(moyenneT.plot())
#print(moyenneB.plot())

# Dataframe no2/Tours pour les graphs Seaborn
ntours= df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_no2"].reset_index()
#print(ntours)

# SEABORN
#plt.figure(figsize=(40, 20))

# Graph moyenne no2 par mois pour Tours
#sns.relplot(x="mois", y="val_no2", kind="line", data=ntours)

# Graph moyenne no2 pour les 3 annees pour Tours
#sns.relplot(x= "annee", y="val_no2", kind= "line", data=ntours)

# Graph moyenne no2 pour annee 2018 par mois pour Tours
#sns.relplot(x="mois", y="val_no2", kind="line", data=ntours.query("annee == '2018'"))

# PLOTLY
#plo = px.ntours.gapminder().query("annee == '2018'")
fig = px.line(data_frame=(ntours), x="mois", y="val_no2")
fig.show()
