# Global Renewable Energy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#NOTE: Load the data. 
renew_energy = pd.read_csv('complete_renewable_energy_dataset.csv')
#print(renew_energy.head())

#NOTE: The Year column is set as int64 but we won't perform maths on this column so we can change it into object. 
renew_energy.Year = renew_energy.Year.astype('object')
#print(renew_energy.dtypes)

#NOTE: Let's check if any of our columns have missing or null values.
#print(renew_energy.isnull().sum()) # since all the columns show 0 values we don't have any missing or null values in the DataFrame. 

#NOTE: In order to work more comfortable and efficience we can sort the DataFrame based on the Year column. 
renew_energy.sort_values(by=['Year'], ascending=False, inplace=True)
#print(renew_energy.head())

#NOTE: Now we're going to answer some important questios about the renewable energy.

# What is the total production of energy per country?
# What is the year that country had this production of energy?
# What type of energy is involved?

#NOTE: we can create a define fuction to respond all this questions using information from the Data. 
def total_production(country, year, energy):
    total_prod = renew_energy.loc[(renew_energy["Country"] == country) & (renew_energy["Year"] == year) & (renew_energy["Energy Type"] == energy)]

    print(f"{country} had a total production of {energy} energy in {year} equivalent to:")    
    print(np.round(total_prod["Production (GWh)"].sum()))

#total_production('Japan', 2000, 'Solar')

#NOTE: In order to calculate the total production of energy for each country we group by diff columns. 
total_energy_production = renew_energy.groupby(['Country','Year'], as_index=False)['Production (GWh)'].sum()
production_2000 = total_energy_production[total_energy_production['Year'] == 2000]
production_2023 = total_energy_production[total_energy_production['Year'] == 2023]
#print(production_2000)

#NOTE: Our first analytic would be to see the energy production for each Country in 2000. 

production_2000 = production_2000.sort_values(by='Production (GWh)', ascending=False)
fig, ax = plt.subplots(figsize=(12,8))
#ax = plt.subplot(figsize=(12,8))
bars_00 = plt.bar(range(len(production_2000)), production_2000['Production (GWh)'], color='Orange')
ax.set_xticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
ax.set_xticklabels(production_2000.Country, rotation=30)
ax.bar_label(bars_00)
plt.ylabel('Energy Production (GWh)')
plt.title("Global Renewable Energy Production 2000.")
#plt.show()
plt.clf()
plt.close()

#NOTE: Then we need to check the energy production for each Country in 2023. 

production_2023 = production_2023.sort_values(by='Production (GWh)', ascending=False)
fig, ax = plt.subplots(figsize=(12,8))
#ax = plt.subplot(figsize=(12,8))
bars_23 = plt.bar(range(len(production_2023)), production_2023['Production (GWh)'], color='Yellow')
ax.set_xticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
ax.set_xticklabels(production_2023.Country, rotation=30, fontsize=14)
ax.bar_label(bars_23, fontsize=14)
plt.ylabel('Energy Production (GWh)', fontsize=16)
plt.title("Global Renewable Energy Production 2023.", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#NOTE: In order to have a clear comparation between the energy production we made Stacked Bars.
fig, ax = plt.subplots(figsize=(12,8))
#ax = plt.subplot(figsize=(12,8))
plt.bar(range(len(production_2000)), production_2000['Production (GWh)'], color='Blue', label='2000')
plt.bar(range(len(production_2023)), production_2023['Production (GWh)'],bottom=production_2000['Production (GWh)'], color='Red', label='2023')
ax.set_xticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
ax.set_xticklabels(production_2023.Country, rotation=30, fontsize=14)
plt.ylabel('Energy Production (GWh)', fontsize=16)
plt.title("Global Renewable Energy Production 2000 vs 2023.", fontsize=22)
plt.legend()
#plt.show()
plt.clf()
plt.close()

#NOTE: It is important to determine which country made the mayor investment in USD and that year.
max_investment = renew_energy.groupby(['Country', 'Year'], as_index=False)['Investments (USD)'].max()
#print(max_investment.max()) #The mayor investment in dollars were made by USA in 2023. 

investments = renew_energy.groupby(['Country', 'Year'],as_index=False)['Investments (USD)'].sum()
#print(investments)

investments_in_2000 = investments[investments['Year'] == 2000]
investments_in_2023 = investments[investments['Year'] == 2023]

#NOTE: Let's check the investments by each Country in 2000.

investments_in_2000 = investments_in_2000.sort_values(by='Investments (USD)')
fig, ax = plt.subplots(figsize=(12,8))
#ax = plt.subplot(figsize=(12,8))
inv_00 = plt.barh(range(len(investments_in_2000)), investments_in_2000['Investments (USD)'], color='Green')
ax.set_yticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
ax.set_yticklabels(investments_in_2000.Country, fontsize=14)
ax.bar_label(inv_00,fontsize=14)
ax.spines[['right', 'bottom']].set_visible(False)
plt.ylabel('Investments (USD)',fontsize=16)
plt.title('Countries Investments (USD) in 2000.', fontsize=22)
#plt.show()
plt.clf()
plt.close()

#NOTE: Let's check the investments by each Country in 2023.

investments_in_2023 = investments_in_2023.sort_values(by='Investments (USD)')
fig, ax = plt.subplots(figsize=(12,8))
#ax = plt.subplot(figsize=(12,8))
inv_23 = plt.barh(range(len(investments_in_2023)), investments_in_2023['Investments (USD)'], color='Orange')
ax.set_yticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
ax.set_yticklabels(investments_in_2000.Country, fontsize=14)
ax.bar_label(inv_23, fontsize=14)
ax.spines[['right', 'bottom']].set_visible(False)
plt.ylabel('Investments (USD)', fontsize=16)
plt.title('Countries Investments (USD) in 2023.', fontsize=22)
#plt.show()
plt.clf()
plt.close()



