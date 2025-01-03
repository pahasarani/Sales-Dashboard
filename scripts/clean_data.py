import pandas as pd

# Load the dataset
data = pd.read_excel("Superstore_Sales.xlsx")

# Select relevant columns
data = data[["Order Date", "Sales", "Category", "Region"]]

# Convert 'Order Date' to datetime format
data["Order Date"] = pd.to_datetime(data["Order Date"])

# Add a 'Year' column for aggregation
data["Year"] = data["Order Date"].dt.year

# Save the cleaned data
data.to_csv("cleaned_superstore_data.csv", index=False)

print("Data cleaning complete. Saved as 'cleaned_superstore_data.csv'")
