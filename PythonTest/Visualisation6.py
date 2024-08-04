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

import pandas as pd
import matplotlib.pyplot as plt

#ProductGroupData
# Calculate the number of products in each group
product_group_counts = product_group_data['GroupName'].value_counts()

# Draw a bar chart
plt.figure(figsize=(12, 6))
product_group_counts.plot(kind='bar')
plt.title('Number of Products in Each Group')
plt.xlabel('Product Group')
plt.ylabel('Number of Products')
plt.grid(True)
plt.show()
