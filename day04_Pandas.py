import pandas as pd

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

df = pd.read_csv("students.csv")
print(df)
