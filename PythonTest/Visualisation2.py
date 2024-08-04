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

#Website Access Category
# Count the number of visits by each device type
device_access = website_access_category1['DeviceType'].value_counts()

#Create a chart of visits by device type
plt.figure(figsize=(10, 6))
device_access.plot(kind='bar', color='orange')
plt.title('Website Access by Device Type')
plt.xlabel('Device Type')
plt.ylabel('Number of Accesses')
plt.grid(True)
plt.show()


