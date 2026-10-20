import pandas as pd
import numpy as np
# Pandas Series - 1D labeled array.
###################################################

marks = pd.Series([85, 92, 67, 78])
print(marks)

# Accessing values
print(marks[0])

# with cusstom index
marks = pd.Series(
  [85, 92, 67],
  index=["Rahul", "Priya", "Aman"]
)
print(marks)

## Pandas DataFrame - 2D labeled data structure.
###################################################

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha"],
    "Age": [20, 21, 19, 20],
    "Marks": [85, 92, 67, 88],
    "City": ["Kanpur", "Lucknow", "Delhi", "Kanpur"]
}
df = pd.DataFrame(data)
print(df)

print(df.shape) #(4, 4)
print(df.columns) #Index(['Name', 'Age', 'Marks', 'City'], dtype='object')
print(df.head(2)) #first 2 rows
print(df.info()) #it display first five rows by default

print(df["Name"])
print(df[["Name", "Marks"]])


# Reading CSV Files (Comma-Separated Values)
################################################
#For example, imagine a file named students.csv containing:

#Exercise 1 — Explore the data
df = pd.read_csv("students.csv")
print(df)
print(df.head()) # first five rows
print(df.shape)
print(df.columns)
print(df.dtypes)
# The average marks.
print((df["Marks"]).mean())

# Exercise 2 — Filter students
filtered_df = df[df["Marks"] > 80]
print(filtered_df)

# Exercise 3 — Multiple conditions
print("Exercise 3 — Multiple conditions")
filtered_df = df[(df["Marks"] <= 70) & (df["Age"] <= 21)]
print(filtered_df)

# Exercise 4 — Basic aggregation
# The maximum marks.
print("Max_marks",df["Marks"].max())
# The minimum marks.
print("Min_marks",df["Marks"].min())
# The average marks.
print("Avg_marks",df["Marks"].mean())
# The total number of students.
print("size_students",df["Name"].size)

# Exercise 5 — Filtering with NumPy
marks = df["Marks"].to_numpy()
print(marks[marks>80])



# Challenge 1: Filtering
df = pd.read_csv("students.csv")
# Find all students who:
# - Scored at least 75 marks.
# - Are younger than 21.
# Store the result in qualified_students.
qualified_students = df[(df["Marks"] >= 75) & (df["Age"] <= 21)]
print(qualified_students)
# Challenge 2: NumPy connection
# Convert the Marks column into a NumPy array and calculate the sum of marks greater than 80.
# Do not use a Pandas aggregation for this one.
marks = df["Marks"].to_numpy()
highest_marks = marks[marks > 80]
sum_of_highest_marks = highest_marks.sum()
print("sum : ",sum_of_highest_marks)
# Challenge 3: Aggregation
# Calculate the average marks of students from Kanpur only.
# Hint: Filter the rows by city first, then calculate the mean of their Marks.
kanpur_student = df[(df["City"]=="Kanpur")]
print(f"Avg : {kanpur_student["Marks"].mean():.2f}")
# Challenge 4: Your first real data-analysis question
# Which city has the highest average student marks?
student = df[["City","Marks"]]
print(student)
kanpur_marks = df[(df["City"]=="Kanpur")]
delhi_marks = df[(df["City"]=="Delhi")]
Lucknow_marks = df[(df["City"]=="Lucknow")]
print(kanpur_student["Marks"].mean())
print(delhi_marks["Marks"].mean())
print(Lucknow_marks["Marks"].mean())
# For now, solve this using filtering and .mean()—you don't need groupby() yet. We'll learn groupby() in Day 4.






df = pd.read_csv("students.csv")

# 1. Selecting columns and rows: .loc vs .iloc
########################################################
print(df)
print("loc",df.loc[0:2, ["Name", "Marks"]])
print("iloc",df.iloc[0:3, 0:3])

# 2. Filtering data
########################################################
# Students with marks above 80
print(df[df["Marks"] > 80])
# Students from Kanpur
print(df[df["City"] == "Kanpur"])
# Students aged 20 or younger who scored at least 75
print(df[(df["Age"] <= 20) & (df["Marks"] >= 75)])

print(df[df["City"].isin(["Kanpur", "Delhi"])])

# 3. Handling missing values
data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha"],
    "Age": [20, 21, None, 20],
    "Marks": [85, None, 67, 88],
    "City": ["Kanpur", "Lucknow", None, "Kanpur"]
}

df = pd.DataFrame(data)
print(df.isna())
print(df[df["Marks"].isna()])
# df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# df["City"] = df["City"].fillna("Unknown")
print(df.dropna(subset=["Marks"]))
# print(df)
print(df[pd.isnull(df["City"])])


df = pd.read_csv("students.csv")
# 4. groupby() — one of the most useful Pandas skills
########################################################
print(df.groupby("City")["Marks"].mean())
print(df.groupby("City")["Marks"].agg(["mean", "max", "min", "count"]))
print(df.groupby(["City", "Age"])["Marks"].mean())
print(df["City"].value_counts(normalize=True))

# quiz
# Select rows and columns
# Use .loc to select the rows with index labels 1 through 4, inclusive, and display only Name and Marks.
print(df.loc[1:4, ["Name", "Marks"]])

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha"],
    "Age": [20, 21, None, 20],
    "Marks": [85, None, 67, 88],
    "City": ["Kanpur", "Lucknow", None, "Kanpur"]
}
df = pd.DataFrame(data)
# Handle missing values
# - Count missing values in each column.
# - Fill missing Marks with the mean of the available marks.
# - Print the updated Marks column.
# Hint: isna().sum() and fillna().
print(df.isna().sum())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print(df["Marks"])
print(df)

# Group and aggregate
# For each city, calculate:
# - Average marks
# - Maximum marks
# - Number of non-missing marks
# Hint: Combine groupby() with agg().
print(df.groupby("City")["Marks"].agg(["mean", "max", "count"]))

# Sort the students
# Display the full DataFrame with marks sorted from highest to lowest.
print(df.sort_values(by="Marks", ascending=False))

# Count categories
# Count how many students belong to each city. Then calculate the proportion of students from each city.
print(df["City"].value_counts())
print(df["City"].value_counts(normalize=True))