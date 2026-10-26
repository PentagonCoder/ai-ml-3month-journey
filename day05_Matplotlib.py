import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Marks": [85, 92, 67, 88, 45],
    "StudyHours": [2, 5, 1, 4, 2]
})

days = [1, 2, 3, 4, 5]
hours = df["StudyHours"]

plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.xlabel("Day")
plt.ylabel("Study Hours")
plt.title("Study Hours Over Time")
plt.grid(True)

# Save the plot instead of showing it
plt.savefig("my_plot.png")

print("Plot saved successfully as my_plot.png!")