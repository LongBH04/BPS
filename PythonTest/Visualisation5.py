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


#CustomerData
#Converts the DateOfBirth column to a date format
Customer_Data['DateOfBirth'] = pd.to_datetime(Customer_Data['DateOfBirth'])

# Calculate age
current_date = pd.Timestamp.now()
Customer_Data['Age'] = (current_date - Customer_Data['DateOfBirth']).dt.days // 365

# Draw an age distribution histogram
plt.figure(figsize=(12, 6))
Customer_Data['Age'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.grid(True)
plt.show()