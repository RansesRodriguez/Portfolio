# Motor Vehicle Collisions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vehicules_collisions = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes.csv")

#NOTE: Drop the columns with too much null or empty values. 
vehicules_collisions.drop({'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5'}, axis='columns', inplace=True)
vehicules_collisions.drop({'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5'}, axis='columns', inplace=True)
vehicules_collisions.drop({'CROSS STREET NAME', 'OFF STREET NAME'}, axis='columns', inplace=True)

#NOTE: Fill the columns with less missing values to work properly. 
vehicules_collisions["BOROUGH"].fillna(value='Unspecified')
vehicules_collisions["ZIP CODE"].fillna(value='Unspecified')
vehicules_collisions["LATITUDE"].fillna(value='Unspecified')
vehicules_collisions["LONGITUDE"].fillna(value='Unspecified')
vehicules_collisions["LOCATION"].fillna(value='Unspecified')
vehicules_collisions["ON STREET NAME"].fillna(value='Unspecified')
vehicules_collisions["CONTRIBUTING FACTOR VEHICLE 1"].fillna(value='Unspecified')
vehicules_collisions["CONTRIBUTING FACTOR VEHICLE 2"].fillna(value='Unspecified')
vehicules_collisions["VEHICLE TYPE CODE 1"].fillna(value='Unspecified')
vehicules_collisions["VEHICLE TYPE CODE 2"].fillna(value='Unspecified')

#NOTE: Now just drop the null info that fill not afect our data.
vehicules_collisions = vehicules_collisions.dropna()

#print(vehicules_collisions.isnull().sum())

#print(vehicules_collisions.head())

#print(vehicules_collisions.BOROUGH.unique())
borough = vehicules_collisions.BOROUGH

#NOTE: Plot a bar graph of the diff Boroughs.

fig, ax = plt.subplots(figsize=(12,8))
#ax = plt.subplot(figsize=(12,8))
plt.bar(borough.unique(), borough.value_counts().values, capsize=5)

ax.set_xticks(range(len(borough.unique())))
ax.set_xticklabels(['MANHATTAN', 'QUEENS', 'BRONX', 'STATEN ISLAND', 'BROOKLYN'], fontsize=16)
plt.ylabel('Boroughs', fontsize=16)
plt.title("Accidents registed by Borough", fontsize=18)
#plt.show()
plt.clf()
plt.close()

#NOTE: Review the mean of people that has been injured during car accidents. 

vehicules_collisions['NUMBER OF PERSONS INJURED'] = vehicules_collisions['NUMBER OF PERSONS INJURED'].astype('int64')
#print(vehicules_collisions["NUMBER OF PERSONS INJURED"].unique())
#print(vehicules_collisions.info())

people_injured = np.round(vehicules_collisions['NUMBER OF PERSONS INJURED'].max())
#print(f"The maximum number of people injured during car accidents in the State of NY from 2012 to 2024 is {people_injured}")

#NOTE: Plot a bar graph showing the people injured in the State of NY per year. 

# First, split the CRASH DATE column to use the year data. 
date_split = vehicules_collisions["CRASH DATE"].str.split("/")

vehicules_collisions["YEAR"] = date_split.str.get(2)
vehicules_collisions.sort_values(by=('NUMBER OF PERSONS INJURED'), ascending=False, inplace=True)
most_injured = vehicules_collisions['NUMBER OF PERSONS INJURED'][0:13]
#print(most_injured)

fig, ax = plt.subplots(figsize=(12,8))
#ax = plt.subplot(figsize=(12,8))

plt.bar(vehicules_collisions.YEAR.unique(), most_injured, capsize=5)
plt.title("Number of People Injured per Year.", fontsize=16)
#plt.show()
plt.clf()
plt.close()

#NOTE: Last but not least, let's plot a bar graph about the contibuting factor fot the vehicles collisions. 

factors = vehicules_collisions['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()
factor_example = factors[1:11]
#print(factor_example.keys())

fig, ax = plt.subplots(figsize=(10,6))
#ax = plt.subplot(figsize=(20,8))

plt.bar(range(len(factor_example.unique())), factor_example.values, capsize=8)

plt.xticks(range(len(factor_example.unique())), ['Driver Distraction', 'Yield Right of Way', 'Follow too closely',\
                                                  'Other Vehicle', 'Backing Unsafely', 'Turning Bad', 'Fatigued', \
                                                    'Traffic Control Disregarded', 'Passing', 'Lost Consciousness'], fontsize=8, rotation=40)
plt.title('10 Most Frequent Accident Factors in NY', fontsize=18)
plt.ylabel('CONTRIBUTING FACTOR VEHICLE')
#plt.show()
plt.clf()
plt.close()

#NOTE: In order to work properly with this data, let's set a 100 dataset. 

vehicules_collisions[0:50].to_csv('collisions.csv')
