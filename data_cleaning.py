import pandas as pd

# Load dataset
data = pd.read_csv("employees.csv")

# Remove duplicate rows
data = data.drop_duplicates()

# Fill missing values
data = data.fillna(method="ffill")

# Save cleaned dataset
data.to_csv("cleaned_employees.csv", index=False)

print("Data cleaning completed successfully!")
