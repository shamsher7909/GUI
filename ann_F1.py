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

# Assuming you have trained your ANN model and obtained the history object
# Access the loss values from the history object
loss = history.history['loss']

# Get the number of epochs
epochs = range(1, len(loss) + 1)

# Plot the epochs versus loss
plt.plot(epochs, loss, 'b-', label='Training Loss')
plt.title('Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
In the above code, the loss variable stores the training loss values from the history object. The epochs variable represents the number of epochs. Then, using Matplotlib, the epochs are plotted on the x-axis and the corresponding loss values on the y-axis.

You can customize the plot by adding a title, x-axis and y-axis labels, and a legend. Finally, the plt.show() function is used to display the plot.

Note: Make sure you have the matplotlib library installed in your Python environment. If not, you can install it using the command pip install matplotlib.










