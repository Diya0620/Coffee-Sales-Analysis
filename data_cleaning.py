
import pandas as pd

# Load the dataset
file_path = "data/Afficionado Coffee Roasters.xlsx"
df = pd.read_excel(file_path)

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Create Revenue column
df["revenue"] = df["transaction_qty"] * df["unit_price"]

# Extract transaction hour
df["transaction_hour"] = pd.to_datetime(
    df["transaction_time"], format="%H:%M:%S"
).dt.hour

# Display updated dataset
print("\nUpdated Dataset:")
print(df.head())

# Check total revenue
print("\nTotal Revenue:")
print(df["revenue"].sum())

# Check average transaction revenue
print("\nAverage Revenue:")
print(df["revenue"].mean())

# Save cleaned dataset
df.to_csv("data/cleaned_coffee_sales.csv", index=False)

print("\nCleaned dataset saved successfully!")
