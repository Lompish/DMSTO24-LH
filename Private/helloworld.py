
""" 
# Importera pandas
import pandas as pd
# Kontrollera att pandas fungerar:
print(pd.__version__)

# Skapa en DataFrame med pandas
# Exekvetera filen med: python 03-pandas.py

# Data en dictionairy med nyckel för column rubrik
#Och lista på värden per rad
data = {
    "Name": ["Anna", "Björn", "Cecilia"],
    "Age": [25, 30, 27],
    "City": ["Stockholm", "Göteborg", "Malmö"]
}
df = pd.DataFrame(data)
print(df)
print(df.info())

# Gör något med kolumnen Age
print("Gör något med kolumnen Ages:")
ages = df["Age"]
print(ages)

print("Alla äldre än 25:")
filtered_data = df[df["Age"] > 25]
print(filtered_data)

print("Alla yngre än eller exakt 25:")
filtered_data = df[df["Age"] <= 25]
print(filtered_data)


#print("Antalet element:")
#len(ages)

# Summera alla åldrar i kolumnen Age
summa = df["Age"].sum()
# Räknar antal rader
antal = df["Age"].count()
print(summa)
print(antal)

# vi gör en beräkning:
print("Egen beräkning:")
print(summa/antal)

# eller vi använder inbyggda funktioner
print("Inbyggd beräkning för medelvärde:")
print(df["Age"].mean())

print("Eller median:")
print(df["Age"].median())
"""

"""
import pandas as pd

data = {
   "City": ["Stockholm", "Göteborg", "Stockholm", "Malmö"],
   "Sales": [100, 200, 150, 300]
}
df = pd.DataFrame(data)

grouped = df.groupby("City")["Sales"].sum()
print(grouped)


# ii . öppnar mapphanteraren för windows

import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)
"""

# Stapeldiagram
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt

data = {"Category": ["A", "B", "C"], "Values": [10, 20, 15]}
df = pd.DataFrame(data)

sns.barplot(x="Category", y="Values", data=df)
plt.show()