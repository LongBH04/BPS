import pandas as pd

#Loading the data
dataFrame = pd.read_csv("E:\SE06204\Business Process Support\ASM\CustomerData.csv")
print(dataFrame)

#missing_data = df.isnull().sum()
missing_data = dataFrame.isnull().sum()
print("Missing data in each column:\n", missing_data)

#Save the cleaned data
dataFrame.to_csv("E:\SE06204\Business Process Support\ASM\CustomerData.csv", index=False)
print("Data cleaning and preprocessing completed. Cleaned data saved to 'E:\SE06204\Business Process Support\ASM\CustomerData.csv'.")
