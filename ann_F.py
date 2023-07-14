import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense


from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.stats import pearsonr


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



# Plotting the prediction and response values
plt.plot(prediction_df['Prediction'], label='Prediction')
plt.plot(prediction_df['Response'], label='Response')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Prediction vs Response')

# Add legend
plt.legend()

# Display the plot
plt.show()

# Print the DataFrame
print(prediction_df)


# Calculate RMSE
rmse = np.sqrt(mean_squared_error(prediction_df['Response'], prediction_df['Prediction']))

# Calculate MAE
mae = mean_absolute_error(prediction_df['Response'], prediction_df['Prediction'])

# Calculate correlation coefficient R
r, _ = pearsonr(prediction_df['Response'], prediction_df['Prediction'])

# Print metrics
print('Root Mean Squared Error (RMSE):', rmse)
print('Mean Absolute Error (MAE):', mae)
print('Correlation Coefficient R:', r)



