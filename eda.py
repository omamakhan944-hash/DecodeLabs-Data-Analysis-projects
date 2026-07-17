import pandas as pd

# Load cleaned dataset
data = pd.read_csv("cleaned_employees.csv")

print("First Five Rows")
print(data.head())

print("\nDataset Information")
print(data.info())

print("\nStatistical Summary")
print(data.describe())

print("\nMissing Values")
print(data.isnull().sum())
