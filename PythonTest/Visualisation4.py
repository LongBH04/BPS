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


#ProductDetailData
# Combine data of ProductDetailData and Product_GroupData
merged_data = pd.merge(product_details, product_group_data, on='ProductGroupID')

# Calculate the average price by product group
average_price_by_group = merged_data.groupby('GroupName')['Price'].mean()

#Draw a bar chart
plt.figure(figsize=(12, 6))
average_price_by_group.plot(kind='bar')
plt.title('Average Price of Products by Group')
plt.xlabel('Product Group')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()
