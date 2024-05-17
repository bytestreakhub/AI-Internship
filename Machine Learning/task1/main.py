import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load the historical stock market data
df = pd.read_csv('stocks\A.csv')

# Use technical indicators like 'Open', 'High', 'Low', 'Volume'
features = ['Open', 'High', 'Low', 'Volume']
X = df[features]
y = df['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the algorithm
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regressor.predict(X_test)

# Compare the actual output values with the predicted values
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)
