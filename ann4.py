import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Load the CSV file
data = pd.read_csv('training.csv')

# Extract input variables (X) and response variable (y)
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Variable names
variable_names = list(data.columns[:-1])

# Create the model
model = Sequential()
model.add(Dense(8, input_dim=5, activation='relu'))  # Adjust the number of nodes and input_dim based on your preference
model.add(Dense(1, activation='linear'))  # Use 'linear' activation for regression tasks

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fit the model to the data
model.fit(X, y, epochs=100, batch_size=32)  # Adjust the number of epochs and batch_size based on your preference

# Make predictions
predictions = model.predict(X)

# Create a DataFrame with predictions, actual response, and input variables
prediction_df = pd.DataFrame({'Response': y, 'Prediction': predictions.flatten()})
prediction_df[variable_names] = data.iloc[:, :-1]

# Save predictions to Excel file
#prediction_df.to_excel('predictions.xlsx', index=False)
prediction_df.to_json('predictions.json', orient='records')

prediction_df.to_csv('predictions.csv', index=False)

