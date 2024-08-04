import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load CSV files
data = pd.read_csv("E:/SE06204/Business Process Support/ASM/SaleData.csv")

# Data Preprocessing
# Check for missing values and handle them
print(data.isnull().sum())
data = data.dropna()

# Define features and target variable
X = data[['Quantity', 'UnitPrice']]  # Features
y = data['TotalPrice']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predictions')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Perfect Prediction')
plt.xlabel('Actual Total Price')
plt.ylabel('Predicted Total Price')
plt.title('Predicted vs Actual Total Price')
plt.legend()
plt.grid(True)
plt.show()
