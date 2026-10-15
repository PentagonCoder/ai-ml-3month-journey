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


# Part 1 — Boolean Masking and Filtering

marks = np.array([35, 80, 45, 90, 25, 70, 95])
print(marks[marks > 60]) # [80 90 70 95]
print(marks[marks == 70]) # [70]
print(marks[marks != 70]) # [35 80 45 90 25 95]

print("And ", marks[(marks > 60) & (marks < 90)]) # [80 70]
print("Or ", marks[(marks < 40) | (marks > 90)]) # [35 25 95]
mark = marks > 60
print(mark) # [False  True False  True False  True  True]

# Part 2 — Reshape and Transpose

# reshape() reorganizes elements according to the specified shape and traversal order.
a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape(3, 2))
print(a.reshape(2, -1))
print(a.reshape(-1, 2))
print(a)

# transpose() rearranges the array's axes.
b = a.reshape(2, 3)
print("Original shape:", b)
print("Transposed shape:", b.T)

# Part 3 — Aggregate Functions
print(np.sum(a))
print(np.mean(a))
print(np.min(a))  
print(np.max(a))
print("Standard deviation:", np.std(a)) # by default ddof = 0


# Why does standard deviation matter in ML?
a = np.array([48, 49, 50, 51, 52])
b = np.array([10, 30, 50, 70, 90])

# both has same mean
print("Mean of a:", np.mean(a))
print("Mean of b:", np.mean(b))
# but different standard deviation

print("Standard deviation of a:", np.std(a)) # a has smaller deviation mean value than b
print("Standard deviation of b:", np.std(b))



# 3.2 Aggregation along an axis
a = np.array([
  [10, 20, 30],
  [40, 50, 60]
])

print(np.sum(a, Axis=0))  # sum along columns
print(np.sum(a, Axis=1))  # sum along rows
print(np.mean(a))
print(np.min(a))  
print(np.max(a))