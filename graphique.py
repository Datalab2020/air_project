#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:11:13 2020

@author: formateur
"""

import pandas as pd
import plotly.graph_objects as go
import numpy as np


url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

df["jour"] = pd.DatetimeIndex(df["date_ech"]).day
df["mois"] = pd.DatetimeIndex(df["date_ech"]).month
df["an"] = pd.DatetimeIndex(df["date_ech"]).year
df["axe"] = df["an"].astype(str) + df["mois"].astype(str)
df["axeTemp"] = df["axe"].astype(int)
dfGroup = df.groupby(["lib_zone", "an", "mois", "axeTemp"])

dfAgre = dfGroup.agg({"val_no2" : 'mean',
                       "val_so2" : 'mean',
                       "val_o3" : 'mean',
                       "val_pm25" : 'mean',
                       "val_pm10" : 'mean'})

dfFin = dfAgre.reset_index()
dfFin= dfFin[dfFin.lib_zone == "BLOIS"]
dfUlt = dfFin.T

