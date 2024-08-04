import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Data
data = pd.read_csv("E:/SE06204/Business Process Support/ASM/SaleData.csv")

# Step 2: Display the Data
print(data.head())
print(data.info())

# Step 3: Handle Missing Values
# Fill missing values with the mean for numerical columns
data.fillna(data.mean(numeric_only=True), inplace=True)

# Step 4: Check for Date and Sales Columns
date_column = 'SaleDate'  # Date column name in your data
sales_column = 'TotalPrice'  # Sales column name in your data

if date_column in data.columns and sales_column in data.columns:
    # Convert Date Column to DateTime
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')
    
    # Drop rows where date conversion failed
    data.dropna(subset=[date_column], inplace=True)
    
    # Convert Date Column to Numeric (days since the minimum date)
    data[date_column] = (data[date_column] - data[date_column].min()) / pd.Timedelta(days=1)
    
    # Step 5: Create Line Chart
    plt.figure(figsize=(12, 6))
    plt.plot(data[date_column], data[sales_column], marker='o', linestyle='-', color='b')
    plt.title('Total Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.show()
    
    # Step 6: Save the Processed Data
    data.to_csv("E:/SE06204/Business Process Support/ASM/Processed_SaleData.csv", index=False)
else:
    print(f"Columns '{date_column}' or '{sales_column}' not found in the data.")
