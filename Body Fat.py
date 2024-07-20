# Body Fat

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

body_fat = pd.read_csv("bodyfat.csv")

#NOTE: Carefully review the DataFrame information.

#print(body_fat.head())
#print(body_fat.describe())
#print(body_fat.info())

#NOTE: First let's start by cleaning the dataset.

#print(body_fat.isna())

duplicates = body_fat.duplicated()
#print(duplicates) #NOTE: No duplicated info found.

#print(body_fat.Age.unique())

body_fat.sort_values(by=["Age"], ascending=True, inplace=True)
#print(body_fat.head())

#NOTE: Calculate the results group by age. 

age_on_20s = body_fat[0:36]
weight = body_fat[0:36]
age_on_30s = body_fat[37:75]
age_40_to_80 = body_fat[76:]

mean_weight_in_20s = np.round(age_on_20s.Weight.mean())
#print(f"The results show the mean weight amoung people from 20 to 29 years old is: {mean_weight_in_20s}lb")

mean_weight_in_30s = np.round(age_on_30s.Weight.mean())
#print(f"The results show the mean weight amoung people from 30 to 39 years old is: {mean_weight_in_30s}lb")

mean_weight_after_40 = np.round(age_40_to_80.Weight.mean())
#print(f"The results show the mean weight amoung people from 40 years old is: {mean_weight_after_40}lb")

#NOTE: Based on the calculations abouve, the mean weight in people on 20 t0 80 years old is around 179lb. 

#NOTE: Weight about the mean.

over_180 = body_fat[body_fat.Weight >= 180]
over_180_mean = np.round(over_180.Weight.mean())
print(over_180_mean)

#NOTE: Let's start of data visualization by doing some plots.

plt.bar(range(len(age_on_20s.Weight.head(10))),age_on_20s.Weight.head(10),0.4, label="Weight")
plt.bar(range(len(age_on_20s.Weight.head(10))),age_on_20s.BodyFat.head(10),0.4,bottom=age_on_20s.Weight.head(10),label="Body Fat")
plt.legend(["Weight", "Body Fat"])
#plt.show()
plt.clf()
plt.close()

#NOTE: The purpose of the plot about is to show the body fat of some of the individuals in the data in relation with their weight.

fat_20 = age_on_20s.BodyFat
fat_more_40 = age_40_to_80.BodyFat

plt.hist(fat_20,color='blue' ,label="20's years old body fat",density=True, alpha=0.5)
plt.hist(fat_more_40, color='red',label="More than 40 years old body fat",density=True,alpha=0.5)
plt.legend()
#plt.show()
plt.clf()
plt.close()

#NOTE: The purpose of the plot about is to show compare the body fat of some of the individuals in the data.
