#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:48:22 2020

@author: formateur
"""

" Projet qualité de l'air en Région Centre "


import pandas as pd
import folium 

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)


print (df)

print(df.info())
print(df.columns)


print (df.loc[:,"lib_zone"])

print (df.loc[:,"valeur"])

