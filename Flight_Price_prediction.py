#Flight_Price_prediction

import pandas as pd
import numpy as np

flight_data = pd.read_csv("flight_dataset.csv")

#print(flight_data.head())

#print(flight_data.describe())

# Double-check if there's missing data in the data set.

#print(flight_data.isnull().value_counts())


# Let's review the non-stop destinantion and the destination with 2 stops and compare duration and prices. 

non_stop_dest = flight_data[flight_data["Total_Stops"] == 0]
print(non_stop_dest.head())

non_stop_mean = round(np.mean(non_stop_dest.Price))
print(f"Mean price for non-stops flights: ${non_stop_mean}")

non_stop_median = round(np.median(non_stop_dest.Price))
print(f"Median price for non-stops flights: ${non_stop_median}")

print("Two stops flight calculations")
two_stops_dest = flight_data[flight_data["Total_Stops"] == 2]
print(two_stops_dest.head())

two_stops_mean = round(np.mean(two_stops_dest.Price))
print(f"Mean price for two stops flights: ${two_stops_mean}")

two_stops_median = round(np.median(two_stops_dest.Price))
print(f"Median price for two stops flights: ${two_stops_median}")

#NOTE: Price for flights with two stops are twice the cost of the non-stop flights. 

import matplotlib.pyplot as plt

plt.hist(non_stop_dest.Price, color='blue', label='Non-Stop', density=True, alpha=0.5)
plt.hist(two_stops_dest.Price, color='green', label='Two Stops', density=True, alpha=0.5)
plt.legend()
plt.title("Non-Stop vs Two Stops flighs at 2019")
#plt.show()
plt.clf()
plt.close()

# Compare the change in the price through the months. 

print("Record of average prices for flights from March to June of 2019")

march_flights = flight_data[(flight_data["Month"] == 3)]
mean_march_flights = round(np.mean(march_flights.Price))
print(f"Mean flights price for March: ${mean_march_flights}")

april_flights = flight_data[(flight_data["Month"] == 4)]
mean_april_flights = round(np.mean(april_flights.Price))
print(f"Mean flights price for April: ${mean_april_flights}")

may_flights = flight_data[(flight_data["Month"] == 5)]
mean_may_flights = round(np.mean(may_flights.Price))
print(f"Mean flights price for May: ${mean_may_flights}")

june_flights = flight_data[(flight_data["Month"] == 6)]
mean_june_flights = round(np.mean(june_flights.Price))
print(f"Mean flights price for June: ${mean_june_flights}")

# Plot the "mean" results to compare the price behavior in 2019. 

Months = ['March', 'April', 'May', 'June']
Mean_Price = [mean_march_flights, mean_april_flights, mean_may_flights, mean_june_flights]

ax = plt.subplot()
plt.bar(range(len(Months)), Mean_Price)
ax.set_xticks(range(len(Months)))
ax.set_xticklabels(Months)
plt.title("Mean price comparison from March to June 2019")
#plt.show()
plt.clf()
plt.close()

#NOTE: As we can appreciate in the bar plot, the price does no flow an specific behavioir to show what could be the prices for the following months. 