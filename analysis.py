import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("student-mat.csv", sep=";")

# Show basic information
print("First 5 students:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nAverage final grade:")
print(data["G3"].mean())

# Plot study time vs final grade
plt.scatter(data["studytime"], data["G3"])
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.title("Study Time vs Final Grade")
plt.show()
