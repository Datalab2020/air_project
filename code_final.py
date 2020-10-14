#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:30:04 2020

@author: formateur
"""
# importation librairies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

# Dataframe
url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

# indexation par mois et années
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["annee"] = pd.DatetimeIndex(df["date_ech"]).year

# Qualif pour Tours
colonnes = "lib_zone", "valeur", "qualif"
print(df.loc[(df["lib_zone"] == "TOURS"), colonnes].sort_values(by=["valeur", "qualif"]))

colonnes = "lib_zone", "qualif"
print(df.loc[(df["lib_zone"] == "TOURS"), colonnes].sort_values(by=["qualif"]))

sns.catplot(x="lib_zone", y="valeur", kind="bar", data=df)


# Valeurs polluants pour Tours dans le temps croissant
tours =  "lib_zone", "date_ech", "val_no2", "val_so2", "val_o3", "val_pm10"
print(df.loc[(df["lib_zone"] == "TOURS"), tours].sort_values(by=["date_ech"]))

# Moyennes de chaque polluants pour toutes les villes
print(df.groupby(["lib_zone"]).mean()["val_no2"])
print(df.groupby(["lib_zone"]).mean()["val_so2"])
print(df.groupby(["lib_zone"]).mean()["val_o3"])
print(df.groupby(["lib_zone"]).mean()["val_pm10"])

# Moyennes par années et par mois pour chaque polluants indépendants pour Tours
ntours= df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_no2"]
print(df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_so2"])
print(df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_o3"])
print(df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()["val_pm10"])

# Essai 1 fonction sous alias
def moyenne(ville):
    return df.loc[(df["lib_zone"] == ville)].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

print(moyenne("TOURS"))
print(moyenne("BOURGES"))


# Moyennes par années et par mois pour les polluants pour TOURS
moyenneT = df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

# Moyennes par années et par mois pour les polluants pour BOURGES
moyenneB = df.loc[(df["lib_zone"] == "BOURGES")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

# Moyennes par années et par mois pour les polluants pour BLOIS
moyenneBL = df.loc[(df["lib_zone"] == "BLOIS")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

# Moyennes par années et par mois pour les polluants pour CHARTRES
moyenneC = df.loc[(df["lib_zone"] == "CHARTRES")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

# Moyennes par années et par mois pour les polluants pour CHATEAUROUX
moyenneCH = df.loc[(df["lib_zone"] == "CHATEAUROUX")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

# Moyennes par années et par mois pour les polluants pour DREUX
moyenneD = df.loc[(df["lib_zone"] == "DREUX")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

# Moyennes par années et par mois pour les polluants pour MONTARGIS
moyenneM = df.loc[(df["lib_zone"] == "MONTARGIS")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]

# Moyennes par années et par mois pour les polluants pour ORLEANS
moyenneO = df.loc[(df["lib_zone"] == "ORLEANS")].groupby(["annee", "mois"]).mean()[["val_no2", "val_so2", "val_o3", "val_pm10", "val_pm25"]]


# Graphiques de la moyenne des polluants sur 3 ans

graphT= moyenneT.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR TOURS", xticks=np.arange(0, 34, 3))
fig = graphT.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphT")

graphB= moyenneB.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR BOURGES", xticks=np.arange(0, 34, 3))
fig = graphB.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphB")

graphBL= moyenneBL.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR BLOIS", xticks=np.arange(0, 34, 3))
fig = graphBL.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphBL")

graphC= moyenneC.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR CHARTRES", xticks=np.arange(0, 34, 3))
fig = graphC.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphC")

graphCH= moyenneCH.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR CHATEAUROUX", xticks=np.arange(0, 34, 3))
fig = graphCH.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphCH")

graphD= moyenneD.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR DREUX", xticks=np.arange(0, 34, 3))
fig = graphD.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphD")

graphM= moyenneM.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR MONTARGIS", xticks=np.arange(0, 34, 3))
fig = graphM.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphM")

graphO= moyenneO.plot(figsize=(15,9), title="MOYENNES DES POLLUANTS SUR 3 ANS POUR ORLEANS", xticks=np.arange(0, 34, 3))
fig = graphO.get_figure()
axes = plt.gca()
axes.set_xlabel("TEMPS EN ANNEE/MOIS")
fig.autofmt_xdate()
axes.set_ylabel("VALEURS")
plt.savefig("graphO")



# Dataframe no2/Tours pour les graphs Seaborn
ntours= df.loc[(df["lib_zone"] == "TOURS")].groupby(["annee", "mois"]).mean()[("val_no2")].reset_index()
print(ntours)

# SEABORN
plt.figure(figsize=(40, 20))

# Graph moyenne no2 par mois pour Tours
sns.relplot(x="mois", y="val_no2", kind="line", data=ntours)

# Graph moyenne no2 pour les 3 annees pour Tours
sns.relplot(x= "annee", y="val_no2", kind= "line", data=ntours)

# Graph moyenne no2 pour annee 2018 par mois pour Tours
sns.relplot(x="mois", y="val_no2", kind="line", data=ntours.query("annee == '2018'"))

group_valeur = df.groupby('lib_zone')['valeur'].mean()
group_valeur.plot(kind='bar') #, legend='Reverse'
plt.ylabel('Valeur')

valeur_max_ville = df.groupby('lib_zone')['valeur'].max()
valeur_max_ville.plot(kind='bar') #, legend='Reverse'
plt.ylabel('Valeur')

