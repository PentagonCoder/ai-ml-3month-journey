# Create a list of 10 numbers (0 to 9)
num = [i for i in range(10)]
# Print the first 3 elements
print(num[0:3])
# Print the last 3 elements
print(num[-3:])
# Print every second element
print([i for i in num if i%2==0])
# Reverse the list
num.reverse()
print(num)

# Write a function that takes a list of numbers and returns:
# - the sum◘
def num_sum(n):
  total = 0
  for i in n:
    total += i
  return total
print(num_sum(num))

# - the average
def num_avg(n):
  total = 0
  for i in n:
    total += i
  return total/len(n)
print(num_avg(num))

# - the maximum value
def num_max(n):
  return max(n)
print(num_max(num))
print(max(num))
# Call the function with your list from exercise 1
def call ( fn , list):
  return fn(list)
print(call(num_avg, num))


# Write a function that takes a number and returns:
# "Positive", "Negative", or "Zero"
def machine_1(n):
  if n > 0:
    return "Positive"
  elif n==0:
    return "Zero"
  return "Negative"
print(machine_1(-32))
# Then create a list of 8 numbers (mix of positive, negative, zero)
numbers = [10, -5, 0, 42, -12, 0, -1, 7]
# Loop through the list and print the label for each number
for i in numbers:
  print(f"number {i}: label = {machine_1(i)}")


# From a list of numbers 1 to 20, create a new list that contains only the even numbers
print([i for i in range(1,21) if i%2==0])
# Create another list that contains the squares of numbers from 1 to 10
print([i**2 for i in range(1,11)])