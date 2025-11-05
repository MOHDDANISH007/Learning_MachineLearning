import numpy as np

# Create a list with prices
prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Create an empty list for final prices
final_price = []

discount_price_on_each_item = 10

# without broadcasting
for price in prices:
    final_price_data_after_discount = price - (price * discount_price_on_each_item / 100)
    final_price.append(final_price_data_after_discount)

print(f"Final Price without broadcasting: {final_price}")



array_price = np.array(prices)

# with broadcasting
final_price = array_price - (array_price * discount_price_on_each_item / 100)

print(f"Final Price with broadcasting: {final_price}")



# some more operation on array by using broadcasting


array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vector = np.array([10, 20, 30])

result = array + vector
print(f"Array + Vector: {result}")



array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vector = np.array([10, 20, 30])

result = array * vector
print(f"Array * Vector: {result}")


result = array * 2;
print(f"Array * 2: {result}")