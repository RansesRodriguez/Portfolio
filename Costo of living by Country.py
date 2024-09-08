# Costo of living by Country

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cost_living = pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv")
#print(cost_living.head())

#NOTE: We can start by check the null data of our DateSet.

#print(cost_living.isna().sum()) #Apparently we do not count with null data.

#NOTE: It is important to review so other important information like the data type and the general information.

#print(cost_living.info())

#NOTE: By performing the previous step we realized that Country is the only object column so we need to know what are the elements on this column.

#print(cost_living.Country.unique())

#NOTE: Before fully initiate into our dataset work let's check the average cost of groceries around the world.

avg_groceries_cost = round(np.mean(cost_living["Groceries Index"]), 2)
#print(f"The Average cost of the basic groceries around the World laids close to {avg_groceries_cost} dollars.")

#NOTE: Since we have countries for all over the World it would be better practice to separate the countries per groups to determine the cost of living.

#Group 1: North America
columns = ["Cost of Living Index", "Rent Index", "Cost of Living Plus Rent Index", "Groceries Index", "Restaurant Price Index", "Local Purchasing Power Index"]
north_america = cost_living.iloc[[8, 11, 59]]
north_america["Total Cost"] = north_america[columns].sum(axis=1)
avg_cost_living_na = round(np.mean(north_america["Total Cost"]), 2)
#print(north_america)


#NOTE: Plot a bar graph to show the diff between the countries in North America. 
fig, ax = plt.subplots(figsize=(12,8))
n = plt.bar(north_america.Country, north_america["Total Cost"], color='g')
ax.bar_label(n, fontsize=14)
ax.set_xticklabels(north_america.Country,fontsize=16)
plt.ylabel("Cost of Living (USD)", fontsize=16)
plt.title("Cost of Living in North America's Countries", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#Group 2: Central America
central_america = cost_living.iloc[[32,44 ,60, 63]] #Note that there are some countries that does not show in the dataset we are working on. 
central_america["Total Cost"] = central_america[columns].sum(axis=1)
avg_cost_living_ca = round(np.mean(central_america["Total Cost"]),2)
#print(central_america)

#NOTE: Plot a bar graph to show the diff between the countries in Central America. 
fig, ax = plt.subplots(figsize=(12,8))
ca = plt.bar(central_america.Country, central_america["Total Cost"], color='b')
ax.bar_label(ca, fontsize=14)
ax.set_xticklabels(central_america.Country,fontsize=16)
plt.ylabel("Cost of Living (USD)", fontsize=16)
plt.title("Cost of Living in Central America's Countries", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#Group 3: Caribbean Sea
caribbean_sea = cost_living.iloc[[1, 4, 29, 42, 66]] #Note that there are some countries that does not show in the dataset we are working on.
caribbean_sea["Total Cost"] = caribbean_sea[columns].sum(axis=1)
avg_cost_living_cs = round(np.mean(caribbean_sea["Total Cost"]),2)
#print(caribbean_sea)

#NOTE: Plot a bar graph to show the diff between the countries in Caribbean Sea 
caribbean_sea.sort_values(by="Total Cost", ascending=False, inplace=True)
fig, ax = plt.subplots(figsize=(12,8))
cs = plt.bar(caribbean_sea.Country, caribbean_sea["Total Cost"], color='purple')
ax.bar_label(cs, fontsize=14)
ax.set_xticklabels(caribbean_sea.Country,fontsize=16)
plt.ylabel("Cost of Living (USD)", fontsize=16)
plt.title("Cost of Living in Caribbean Sea's Countries", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#Group 4: South America
south_america = cost_living.iloc[[28, 62, 64, 82, 90, 94, 97, 101, 104, 112]] #Note that there are some countries that does not show in the dataset we are working on.
south_america["Total Cost"] = south_america[columns].sum(axis=1)
avg_cost_living_sa = round(np.mean(south_america["Total Cost"]),2)
#print(south_america)

#NOTE: Plot a bar graph to show the diff between the countries in South America
south_america.sort_values(by='Total Cost', ascending=False, inplace=True)
fig, ax = plt.subplots(figsize=(12,8))
sa = plt.bar(south_america.Country, south_america["Total Cost"], color='orange')
ax.bar_label(sa, fontsize=14)
ax.set_xticklabels(south_america.Country,rotation=30 ,fontsize=16)
plt.ylabel("Cost of Living (USD)", fontsize=16)
plt.title("Cost of Living in South America's Countries", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#Group 5: European Union
european_union = cost_living.iloc[[6, 10, 13, 14, 16, 17, 19, 20, 24, 25, 30, 34, 35, 37, 38, 39, 40, 41, 43, 46, 49, 54, 58, 65, 68]]
european_union["Total Cost"] = european_union[columns].sum(axis=1)
avg_cost_living_eu = round(np.mean(european_union["Total Cost"]),2)
#print(european_union)

#NOTE: Plot a bar graph to show the diff between the countries in European Union
european_union.sort_values(by='Total Cost', ascending=True, inplace=True)
fig, ax = plt.subplots(figsize=(12,8))
ea = plt.barh(european_union.Country, european_union["Total Cost"], color='red')
ax.bar_label(ea, fontsize=14)
ax.spines[['top', 'right']].set_visible(False)
plt.xlabel("Cost of Living (USD)", fontsize=16)
plt.title("Cost of Living in European Union's Countries", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#Group 6: Sovereign states
sovereign_states = cost_living.iloc[[72, 73, 77, 85, 91, 95, 99, 100, 103, 113, 115, 118, 119]] #Note that there are some countries that does not show in the dataset we are working on.
sovereign_states["Total Cost"] = sovereign_states[columns].sum(axis=1)
avg_cost_living_ss = round(np.mean(sovereign_states["Total Cost"]),2)
#print(sovereign_states)

#NOTE: Plot a bar graph to show the diff between the countries in Sovereign states
sovereign_states.sort_values(by='Total Cost', ascending=False, inplace=True)
fig, ax = plt.subplots(figsize=(12,8))
ss = plt.bar(sovereign_states.Country, sovereign_states["Total Cost"], color='gold')
ax.bar_label(ss, fontsize=14)
ax.set_xticklabels(sovereign_states.Country,rotation=30 ,fontsize=16)
plt.ylabel("Cost of Living (USD)", fontsize=16)
plt.title("Cost of Living in Sovereing States's Countries", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#Group 7: Asia
asia = cost_living.iloc[[3, 18, 23, 26, 33, 36, 45, 47, 48, 50, 51, 53, 56, 57, 69, 70, 76, 78, 83, 84, 86, 87, 93, 98, 102, 105, 106, 107, 108, 111, 114, 116, 117, 120]] #Note that there are some countries that does not show in the dataset we are working on.
asia["Total Cost"] = asia[columns].sum(axis=1)
#print(asia)

#NOTE: Plot a bar graph to show the diff between the countries in Asia
asia.sort_values(by='Total Cost', ascending=True, inplace=True)
fig, ax = plt.subplots(figsize=(12,8))
a = plt.barh(asia.Country, asia["Total Cost"], color='yellow')
ax.bar_label(a, fontsize=14)
ax.spines[['top', 'right']].set_visible(False)
plt.xlabel("Cost of Living (USD)", fontsize=16)
plt.title("Cost of Living in Asian's Countries", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#NOTE: In order to work on a visualization plataform we can save our work on a new csv file.

north_america.to_csv('north_america.csv')
central_america.to_csv('central_america.csv')
caribbean_sea.to_csv('caribbean_sea.csv')
south_america.to_csv('south_america.csv')
european_union.to_csv('european_union.csv')
sovereign_states.to_csv('sovereign_states.csv')
asia.to_csv('asia.csv')