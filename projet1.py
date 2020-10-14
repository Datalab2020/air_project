#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:48:22 2020

@author: formateur
"""

" Projet qualité de l'air en Région Centre "
"""
https://pandas.pydata.org/docs/getting_started/index.html
"""

import pandas as pd
import folium 




url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

"""
print (df) 
print(df.info())
print(df.columns)
print(df.loc[:, 'valeur'])
print(df['qualif'])
print(df[['type_zone', 'couleur']])
print(df.valeur)
print(df.Y)
print (df.lib_zone.head())
print(df.sort_values(by='valeur').head())
ville = (df.lib_zone)
print(ville)
"""



fig = folium.Figure(width=800, height=500)
map = folium.Map([47.867990, 1.974466], zoom_start = 8.495).add_to(fig)

folium.Marker(location = [48.7488, 1.35995], popup = "notation", tooltip = "DREUX", icon = folium.Icon(color = 'lightred')).add_to(map)








folium.Marker(location = [48.4455, 1.4906], popup = "notation", tooltip = "CHARTRES", icon = folium.Icon(color = 'darkgreen')).add_to(map)
folium.Marker(location = [47.9032, 1.90398], popup = "notation", tooltip = "ORLEANS", icon = folium.Icon(color = 'purple')).add_to(map)
folium.Marker(location = [47.998, 2.73669], popup = "notation", tooltip = "MONTARGIS", icon = folium.Icon(color = 'darkblue')).add_to(map)
folium.Marker(location = [47.5903, 1.32267], popup = "notation", tooltip = "BLOIS", icon = folium.Icon(color = 'blue')).add_to(map)
folium.Marker(location = [47.3944, 0.68286], popup = "notation", tooltip = "TOURS", icon = folium.Icon(color = 'green')).add_to(map)
folium.Marker(location = [47.0797, 2.39623], popup = "notation", tooltip = "BOURGES", icon = folium.Icon(color = 'red')).add_to(map)
folium.Marker(location = [46.8104, 1.69605], popup = "notation", tooltip = "CHATEAUROUX", icon = folium.Icon(color = 'black')).add_to(map)

""" folium.Circle(location = [47.8, 1.5167], radius = 120000).add_to(map) """

map.save('carte_centre.html')



