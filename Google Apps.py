# Google Apps 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

play_store = pd.read_csv("googleplaystore.csv")
#print(play_store.head())

#print(play_store.dtypes)

#NOTE Modify some values that doesn't seems to be correct in or DataFrame based on each column.

play_store["Category"].replace({"1.9":"ART_AND_DESIGN"}, inplace=True)
play_store["Rating"].replace({19.0:1.9}, inplace=True)
play_store["Installs"].replace({'Free': '0'}, inplace=True)
#print(play_store.Installs.value_counts())

#NOTE Check for missing and null values in the DataFrame

#print(play_store.isna().sum())
#print(play_store.info())
#print(play_store.Installs.unique())
#print(play_store[play_store.isnull().any(axis=1)])

#NOTE Check for duplicated values in the DataFrama

duplicated = play_store.duplicated()
#print(duplicated.head())
#print(duplicated.value_counts())

#NOTE Drop all NaN values in the DataFrame

play_store = play_store.dropna()
print(play_store)
#print(play_store.info())
#print(play_store.isna().sum())

print(play_store.info())

#NOTE: Clean the Installs collumn to find the most popular apps.

play_store.Installs.replace('[\+]', '', regex=True, inplace=True)
play_store.Installs.replace('[\,]', '', regex=True, inplace=True)
play_store["Installs"] = play_store["Installs"].astype('int64')
pd.to_numeric(play_store.Installs)

#print(play_store.Installs.head())

#NOTE: Clean the Price column to see which apps was the most expensive.

play_store.Price.replace('[\$]', '',regex=True ,inplace=True)
play_store['Price'] = play_store["Price"].astype('float64')
pd.to_numeric(play_store.Price)
play_store.sort_values(by=["Price"], ascending=False, inplace=True)

#print(play_store.head())

#NOTE: Do some plots to better undestand the Data. 

# Comparetion between Free and Paid Apps.
sns.countplot(play_store["Type"], order=play_store["Type"].value_counts(ascending=True).index)
#plt.show()
plt.clf()
plt.close()

# Top of the most expensive Apps.
ax = plt.subplot()
plt.bar(range(len(play_store.Installs[0:5])), play_store.Installs[0:5])
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(play_store.App[0:5], rotation=15)
plt.ylabel("Installs")
#plt.show()
plt.clf()
plt.close()

# Pie graph of the most expensive Apps.

plt.pie(play_store.Installs[0:5])
plt.legend(play_store.App[0:5])
plt.axis('equal')
#plt.show()
plt.clf()
plt.close()

print(play_store.head())

# Save the clean Data.
play_store.head(200).to_csv('clean_google.csv')