import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
Customer_Data = pd.read_csv("E:\SE06204\Business Process Support\ASM\CustomerData.csv")
market_trend_data = pd.read_csv("E:\SE06204\Business Process Support\ASM\MarketTrendData.csv")
product_group_data = pd.read_csv("E:\SE06204\Business Process Support\ASM\Product_GroupData.csv")
product_details = pd.read_csv("E:\SE06204\Business Process Support\ASM\ProductDetailData.csv")
sale_data = pd.read_csv("E:\SE06204\Business Process Support\ASM\SaleData.csv")
website_access_category1 = pd.read_csv("E:\SE06204\Business Process Support\ASM\WebsiteAccessCategory1.csv")
# Display the first few rows of each DataFrame
print(Customer_Data)
print(market_trend_data)
print(product_details)
print(sale_data)
print(website_access_category1)


#Sale Table
# Convert SaleDate to datetime format
sale_data['SaleDate'] = pd.to_datetime(sale_data['SaleDate'])

# Group by date and sum the total sales
sales_over_time = sale_data.groupby('SaleDate')['TotalPrice'].sum()

# Plot the sales over time
plt.figure(figsize=(12, 6))
plt.plot(sales_over_time.index, sales_over_time.values)
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

