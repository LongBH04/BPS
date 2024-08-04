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


#MarketTrend
# If the date column has a different name like 'StartDate', modify the following code:
market_trend_data['StartDate'] = pd.to_datetime(market_trend_data['StartDate'], errors='coerce')

#Create charts or process data
plt.figure(figsize=(12, 6))
plt.hist(market_trend_data['StartDate'].dropna(), bins=20, edgecolor='black')
plt.title('Market Trend Start Date Distribution')
plt.xlabel('Start Date')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
