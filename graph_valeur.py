# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:59:23 2020

@author: frand
"""

import pandas as pd
import matplotlib.pyplot as plt

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

def compte(ville):
    return df.loc[(df["lib_zone"] == ville)].groupby(["valeur", "qualif"]).size()
#
comBLO = compte("BLOIS")
comBLO.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_BLOIS.png")

comBOU = compte("BOURGES")
comBOU.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_BOURGES.png")

comCHAR = compte("CHARTRES")
comCHAR.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_CHARTRES.png")

comCHAT = compte("CHATEAUROUX")
comCHAT.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_CHATEAUROUX.png")

comDRE = compte("DREUX")
comDRE.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_DREUX.png")

comMON = compte("MONTARGIS")
comMON.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_MONTARGIS.png")

comORL = compte("ORLEANS")
comORL.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_ORLEANS.png")

comTOU = compte("TOURS")
comTOU.plot(kind='bar', figsize= (9,7), title = "Fréquence des valeurs max de polluants") #, legend='Reverse'
plt.xlabel("Valeur")
plt.ylabel('Fréquence')
plt.savefig("Fréquences_TOURS.png")

