import numpy as np 

# number = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# add = number + 5
# print(add)

# creating multiple way arrays
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matrix) 
# print(np.array([1, 2, 3])) 
# print(np.arange(0, 10, 2))
# print(np.zeros(5, dtype=int))
# print(np.ones((2, 3), dtype=int))
# print(np.linspace(0, 10, 5, dtype=float))


# Level 1

# Exercise 1: Create an array containing the numbers 10, 20, 30, 40, and 50.
print("Exercise 1")
exercise1 = np.array([10, 20, 30, 40, 50])
print("The array: ", exercise1)
print("shape of array: ", exercise1.shape)
print("Its number of dimensions : ", exercise1.ndim)
print("Its total number of elements : ", exercise1.size)
print("Its data type : ", exercise1.dtype)
print("\n")

# Exercise 2: Create an array containing all even numbers from 2 through 20.
print("Exercise 2")
exercise2 = np.arange(2,21,2)
print(exercise2)
print("\n")

# Exercise 3: Create an array of 10 evenly spaced numbers between 0 and 1.
print("Exercise 3")
exercise3 = np.linspace(0,1,10)
print(exercise3)
print("\n")

# Exercise 4: Create a 3 × 4 array of zeros and a 2 × 3 array of ones.
print("Exercise 4")
exercise4_1 = np.zeros((3,4))
exercise4_2 = np.ones((2,3))
print(exercise4_1)
print(exercise4_2)
print("\n")

# Level 2 — Indexing and Slicing

a = np.array([
  [10, 20, 30, 40],
  [50, 60, 70, 80],
  [90, 100, 110, 120]
])
print("Exercise 5: ")
print("Exercise 5: ")
print("Exercise 5: ")
print("Print the element 70:", a[1,2])

# Exercise 6: Print the entire second row.
print("Exercise 6: ")
print("Print the entire second row:", a[1])

# Exercise 7: Print the entire third column.
print("Exercise 7: ")
print("Print the entire third column:", a[:,2])

# Exercise 8: Extract this subarray:
#              [[20 30]
#               [50 60]]
print("Subarray:", a[0:2, 1:3])
print("\n")



# Level 3 — Mathematical Operations

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Exercise 9: Calculate:")

print("a + b: ", a+b)
print("a - b: ", a-b)
print("a * b: ", a*b)
print("a / b: ", a/b)
print("a ** 2: ", a**2)
print("min of a: ", np.min(a))
print("max of a: ", np.max(a))
print("mean of a: ", np.mean(a))
print("Sum of a: ", np.sum(a))
print("\n")

# Level 4 — Broadcasting
# Exercise 11: Predict the output before executing this code.
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Exercise 11: ",a + 10)

# Exercise 12: Predict the output and explain why broadcasting works.
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

print("Exercise 12:",a + b)

a = np.ones((3, 3))
b = np.ones((3,))

print(a + b)


# Level 5 — AI/ML Mini-Exercise

# This is the most important exercise of today's session. Suppose you have a model that predicts house prices using:

# y = wx + b 

# Here, x is the house area measured in thousands of square feet, and y is the predicted price in thousands of currency units.

# Your data:

import numpy as np

areas = np.array([1.0, 1.5, 2.0, 2.5, 3.0])

weight = 50
bias = 10

# Your tasks:

# Calculate predictions for all houses using one vectorized expression.
intailly_predictions = weight * areas + bias
print(intailly_predictions)
# Calculate the average predicted price.
avg_intailly_predictions = np.mean(intailly_predictions)
print(avg_intailly_predictions)
# Add 5 to every prediction.
adjusted_prediction = intailly_predictions + 5
print(adjusted_prediction)
# Calculate the difference between the original predictions and the adjusted predictions.
difference = adjusted_prediction - intailly_predictions 
print(difference)

# Exercise 13: Broadcasting
a = np.array([
  [1],
  [2],
  [3]
])

b = np.array([10, 20])

print(a + b)