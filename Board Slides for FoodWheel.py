# Board Slides for FoodWheel

import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv('orders.csv')
restaurants = pd.read_csv('restaurants.csv')

#print(restaurants.head())

#NOTE: Let's start by analyzing or restaurant data.

#print("How many different types of cuisine FoodWheel offers?")
cuisine_count = restaurants.cuisine.nunique()
#print(f"Answer: {cuisine_count}")

#print("How many different restaurants serve that type of cuisine")
diff_cuisines = restaurants.groupby('cuisine').name.count().reset_index()
#print(f"Answer: {diff_cuisines}")

#NOTE: Create a pie chart that shows the different types of cuisines available on FoodWheel.

plt.pie(diff_cuisines.name.values,\
        labels=diff_cuisines.cuisine.values,\
            autopct='%d%%')
plt.axis('equal')
plt.title('Cuisines offered by FoodWheel')
#plt.show()
plt.clf()
plt.close()

#NOTE: Let's inspect our orders dataset.

#print(orders.head())

#NOTE: Tracking the orders made per month can help us determine a trend. 

orders['months'] = orders.date.apply(lambda x: x.split('-')[0])
#print(orders.head())

#NOTE: Calculate the average and standard deviation of the amount spent per month.

avg_orders = orders.groupby('months').price.mean().reset_index()
#print(f"Average orders per month: \n{avg_orders}")

std_orders = orders.groupby('months').price.std().reset_index()
#print(f"Standard devitation for each month: \n{std_orders}")

#NOTE: Create a bar plot that demonstrates the trend in average order size over time.

ax = plt.subplot()
plt.bar(range(len(avg_orders)),
       avg_orders.price,
       yerr=std_orders.price,
       capsize=5)
ax.set_xticks(range(len(avg_orders)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Amount')
plt.title('Average Order Amount Over Time')
#plt.show()
plt.clf()
plt.close()

#NOTE: Create a customer amount DataFrame that stores each customer and how much they order.

customer_amount = orders.groupby('customer_id').price.sum().reset_index()
customer_amount.to_csv('customer_amount.csv')
#print(f"Customers grouped by total amount spent at FoodWheel: \n {customer_amount.head()}")

#NOTE: Create a histgram of the amount spent by each customer over 6 months.

plt.hist(customer_amount.price.values, range=(0,200), bins=(40))
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Amount spent by each customer over 6 months.")
#plt.show()
plt.clf()
plt.close()

#NOTE: Create a barplot for the neighborhood.

fig, ax = plt.subplots(figsize=(20,15))
#ax = plt.subplot(figsize=(20,15))
plt.bar(restaurants['neighborhood'].unique(),
        restaurants['neighborhood'].value_counts().values,
       capsize=5)
ax.set_xticks(range(len(restaurants['neighborhood'].unique())))
ax.set_xticklabels(['Downtown', 'Brooklyn', 'Midtown', 'Chinatown', 'Uptown', 'Queens', 'UWS'], fontsize=18)
plt.ylabel('Restaurant Count', fontsize=20)
plt.title('Neighborhood by Restaurant Count', fontsize=20)
#plt.show()
plt.clf()
plt.close()

