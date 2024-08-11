# Online Business Sales

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#NOTE: Let's start by loading our date. Since we going to be working with 2 datasets we are going to load both of them.

products_sales = pd.read_csv('business.retailsales.csv')
month_sales = pd.read_csv('business.retailsales2.csv')

#print(products_sales)
#print(month_sales)

#NOTE: First we're going to work with the product dataset.
#NOTE: Let's check for null data and clean all needed columns.

#print(products_sales.isna().sum())
#print(products_sales.info())

#NOTE: Let's take a closer look to the product.

#print(products_sales['Product Type'].unique()) #There are 18 different products on the dataset. \

#NOTE: What was the total amount in (USD) sold in product for our dataset between 2017 and 2019?

total_sold = np.round(products_sales['Total Net Sales'].sum())
#print(f"The total net sales 2017 - 2019 reached a total of {total_sold} (USD)")

#NOTE: We can check what is the total net sales by each product.

products = products_sales.groupby(['Product Type'], as_index=False)['Total Net Sales'].sum()

products = products.sort_values(by='Total Net Sales')
fig, ax = plt.subplots(figsize=(12,8))
ps = plt.barh(products['Product Type'], products['Total Net Sales'], color='Green')
ax.bar_label(ps, fontsize=14)
ax.spines[['top', 'right']].set_visible(False)
plt.xlabel("Total Net Sales", fontsize=16)
plt.title("Total Net Sales per Product 2017 - 2019.", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#NOTE: It's also good to check the total returns. 

returns = products_sales.groupby(['Product Type'], as_index=False)['Returns'].sum()

returns = returns.sort_values(by='Returns')
fig, ax = plt.subplots(figsize=(12, 8))
r = plt.barh(returns['Product Type'], returns['Returns'], color='Red')
ax.bar_label(r, fontsize=12, padding=-20, label_type='edge')
ax.spines[['top', 'right']].set_visible(False)
plt.xlabel("Total Returns", fontsize=16)
plt.title("Total Returns per Product 2017 - 2019", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#NOTE: now we can start working with our second dataset. 

#NOTE: First les's check if we got any null data. 

#print(month_sales.isna().sum())

#NOTE: The Year column is set as a float, we can put it as an object.

month_sales['Year'] = month_sales['Year'].astype('object')
#print(month_sales.info())

#NOTE: Now group the data by year and total sales. 
sales_track = month_sales.groupby(['Year'], as_index=False)['Total Sales'].sum()
sales_track.sort_values(by=['Year'], ascending=True, inplace=True)

#NOTE: Plot a graph with the sales per year. 

fig, ax = plt.subplots(figsize=(12,8))
ts = plt.bar(sales_track['Year'], sales_track['Total Sales'], color='Purple')
ax.bar_label(ts, fontsize=14)
ax.set_xticks([2017, 2018, 2019])
plt.ylabel("Total Sales", fontsize=16)
plt.title("Total Sales 2017 - 2019.", fontsize=22)
#plt.show()
plt.clf()
plt.close()

#NOTE: Now let's review the sales on each year per month.

months = month_sales.groupby(['Month', 'Year'], as_index=False)['Total Sales'].sum()
month_ordered = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Sales on 2017
months_17 = months[months['Year'] == 2017]
months_17.index = pd.CategoricalIndex(months_17['Month'], categories=month_ordered, ordered=True)
months_17 = months_17.sort_index().reset_index(drop=True)

fig, ax = plt.subplots(figsize=(12,8))
m17 = plt.barh(months_17['Month'], months_17['Total Sales'], color='Green')
ax.bar_label(m17, fontsize=12)
ax.spines[['top', 'right']].set_visible(False)
plt.xlabel("Total Sales", fontsize=16)
plt.title("Total sales per Months on 2017.", fontsize=22)
#plt.show()
plt.clf()
plt.close()

# Sales on 2018
months_18 = months[months['Year'] == 2018]
months_18.index = pd.CategoricalIndex(months_18['Month'], categories=month_ordered, ordered=True)
months_18 = months_18.sort_index().reset_index(drop=True)

fig, ax = plt.subplots(figsize=(12,8))
m18 = plt.barh(months_18['Month'], months_18['Total Sales'], color='Yellow')
ax.bar_label(m18, fontsize=12)
ax.spines[['top', 'right']].set_visible(False)
plt.xlabel("Total Sales", fontsize=16)
plt.title("Total sales per Months on 2018.", fontsize=22)
#plt.show()
plt.clf()
plt.close()

# Sales on 2019
month_19 = months[months['Year'] == 2019]
month_19.index = pd.CategoricalIndex(month_19['Month'], categories=month_ordered, ordered=True)
month_19 = month_19.sort_index().reset_index(drop=True)

fig, ax = plt.subplots(figsize=(12,8))
m19 = plt.barh(month_19['Month'], month_19['Total Sales'], color='cyan')
ax.bar_label(m19, fontsize=12)
ax.spines[['top', 'right']].set_visible(False)
plt.xlabel("Total Sales", fontsize=16)
plt.title("Total sales per Months on 2019.", fontsize=22)
plt.show()
plt.clf()
plt.close()