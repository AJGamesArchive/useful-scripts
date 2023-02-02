# Import(s)
import random

# Function that takes a list of data and calculates the most profit that can be made
def maxProfit(data: list):
    filteredData = list(data[data.index(min(data)):]);
    profit = int(max(filteredData) - min(data));
    return profit;

# Testing the function
data = list([]);
for i in range(10000):
    data.append(random.randint(1, 50001));
print(maxProfit(data));