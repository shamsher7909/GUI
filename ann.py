import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Dataset as a NumPy array
data = np.array([12,0.152,0,31,49.46611636,163],
[8,0.105,0,31,32.97741091,48],
[12,0.203,0,31,49.46611636,220.070713],
[4,0.152,0,31,16.48870545,18.75],
[4,0.105,0,31,16.48870545,12.3],
[4,0.203,10,31,16.48870545,24.72413793],
[8,0.105,10,31,32.97741091,49.44827586],
[8,0.152,10,31,32.97741091,75.59241288],
[12,0.152,10,31,49.46611636,167.9181034],
[4,0.152,10,31,16.48870545,19.31573276],
[12,0.203,10,31,49.46611636,226.7107776],
[4,0.105,10,31,16.48870545,12.67112069],
[8,0.105,20,31,32.97741091,52.51034483],
[8,0.203,20,31,32.97741091,106.1146552],
[8,0.152,20,31,32.97741091,80.27344933],
[12,0.105,20,31,49.46611636,120.3362069],
[12,0.152,20,31,49.46611636,178.3163793],
[4,0.203,20,31,16.48870545,26.25517241],
[4,0.203,30,31,16.48870545,26.53448276],
[8,0.203,30,31,32.97741091,107.2435345],
[12,0.203,30,31,49.46611636,243.3109392],
[4,0.152,30,31,16.48870545,20.73006466],
[4,0.105,30,31,16.48870545,13.59892241],
[4,0.203,45,31,16.48870545,23.87586207],
[8,0.203,45,31,32.97741091,96.49827586],
[12,0.152,45,31,49.46611636,162.1568966],
[8,0.152,45,31,32.97741091,72.99886566],
[12,0.203,45,31,49.46611636,218.9324162],
[4,0.105,45,31,16.48870545,12.23637931],
[15,0.1,15,32,218.8,100],
[18,0.1,15,32,192.5,159],
[18,0.1,15,32,280,162],
[6,0.1,15,32,87.5,80],
[12,0.1,15,32,218.8,140],
[20,0.1,15,32,315,235],
[18,0.1,15,32,280,220],
[12,0.1,15,32,201.3,179],
[15,0.1,15,32,218.8,200],
[8,0.1,15,32,133,155],
[7,0.15,20,32,128.8,135],
[8,0.15,20,32,117.6,150],
[12,0.15,20,32,157.7,193],
[8,0.12,15,33,133.2,193],
[9,0.1,20,33,132,120],
[6,0.15,20,33,95,300],
[14.7,0.15,20,33,247,235],
[7,0.15,20,33,68.4,133],
[7,0.15,20,33,109.3,150],
[9,0.15,20,33,109.1,230],
[5,0.15,20,33,102.6,100],
[8,0.15,20,33,127.3,150],
[8,0.203,0,34,31.73811095,113],
[4,0.105,0,34,15.86905548,14.2],
[12,0.105,0,34,47.60716643,138.5],
[12,0.152,0,34,47.60716643,198],
[8,0.105,0,34,31.73811095,59],
[4,0.152,10,34,15.86905548,21.99236641],
[4,0.105,10,34,15.86905548,14.52519084],
[8,0.152,10,34,31.73811095,88.58937531],
[8,0.105,10,34,31.73811095,60.35114504],
[12,0.203,10,34,47.60716643,271.1138726],
[6,0.12,15,34,71.2,70],
[6,0.1,15,34,72.2,87],
[6,0.1,15,34,96.9,120],
[7,0.15,20,34,89,135],
[8,0.203,20,34,31.73811095,140.2271552],
[8,0.152,20,34,31.73811095,107.473605],
[12,0.105,20,34,47.60716643,171.8713362],
[12,0.152,20,34,47.60716643,245.7077586],
[7,0.15,20,34,142,227],
[4,0.203,20,34,15.86905548,33.25741379],
[8,0.15,20,34,174.8,200],
[4,0.203,30,34,15.86905548,33.7887931],
[4,0.152,30,34,15.86905548,27.10668103],
[12,0.152,30,34,47.60716643,249.6336207],
[12,0.203,30,34,47.60716643,334.1612781],
[4,0.105,30,34,15.86905548,17.90301724],
[8,0.105,30,34,31.73811095,74.38577586],
[4,0.152,45,34,15.86905548,24.37284483],
[8,0.203,45,34,31.73811095,128.0991379],
[4,0.105,45,34,15.86905548,16.09741379],
[12,0.152,45,34,47.60716643,224.4568966],
[8,0.152,45,34,31.73811095,98.17838869],
[8,0.105,45,34,31.73811095,66.88362069],
[8,0.15,10,35,108.1,139],
[2.3,0.15,10,35,33.1,241],
[6,0.1,10,35,87.4,105],
[6,0.12,15,35,72.2,85],
[8,0.105,15,35,91.2,70],
[8,0.12,15,35,81.7,111],
[6,0.1,15,35,68.4,87],
[13,0.15,15,35,197.6,130],
[7,0.15,20,35,79,197],
[6,0.15,20,35,83.6,435],
[8,0.15,20,35,55.5,200],
[8,0.15,20,35,142.5,220],
[9,0.1,25,35,76,134],
[20,0.1,15,36,268.2,230],
[20,0.15,15,36,277.8,446],
[6,0.15,20,36,57,349],
[6,0.15,20,36,57,300],
[6,0.15,20,36,57,300],
[9,0.1,25,36,133,137],
[4,0.203,0,37,15.13102912,30.5],
[4,0.105,0,37,15.13102912,16.5],
[8,0.152,0,37,30.26205824,103.847183],
[12,0.152,0,37,45.39308736,242],
[12,0.203,0,37,45.39308736,317.1491366],
[12,0.105,0,37,45.39308736,173],
[4,0.203,10,37,15.13102912,30.70265781],
[4,0.105,10,37,15.13102912,16.60963455],
[8,0.203,10,37,30.26205824,131.8704319],
[12,0.203,10,37,45.39308736,319.2564398],
[12,0.105,10,37,45.39308736,174.1495017],
[11,0.1,20,37,285,145],
[13,0.1,20,37,190,144],
[11,0.1,20,37,114,138],
[11,0.1,20,37,228,149],
[11,0.1,20,37,209,160],
[8,0.203,20,37,30.26205824,143.6212625],
[7,0.15,20,37,146.1,187],
[13,0.1,20,37,247,193],
[11,0.1,20,37,285,171],
[8,0.105,20,37,30.26205824,78.93687708],
[8,0.152,20,37,30.26205824,113.8523933],
[4,0.203,20,37,15.13102912,33.43853821],
[9,0.1,20,37,171,160],
[12,0.152,20,37,45.39308736,265.3156146],
[12,0.105,20,37,45.39308736,189.6677741],
[12,0.203,20,37,45.39308736,347.7050335],
[12,0.1,20,37,342,215],
[10,0.1,20,37,190,215],
[4,0.105,20,37,15.13102912,18.089701],
[4,0.203,30,37,15.13102912,33.69186047],
[4,0.152,30,37,15.13102912,27.28488372],
[4,0.105,30,37,15.13102912,18.22674419],
[8,0.203,30,37,30.26205824,144.7093023],
[8,0.152,30,37,30.26205824,114.7149114],
[12,0.105,30,37,45.39308736,191.1046512],
[4,0.203,45,37,15.13102912,30.45946844],
[4,0.152,45,37,15.13102912,24.66717608],
[4,0.105,45,37,15.13102912,16.47807309],
[8,0.152,45,37,30.26205824,103.7091801],
[12,0.203,45,37,45.39308736,316.727676],
[12,0.1,15,38,336,213],
[9,0.1,15,38,171,171],
[6,0.1,20,38,114,93],
[4,0.12,20,38,57,66],
[7,0.15,20,38,81.7,188],
[8,0.114,20,39,193.8,150])

# Split the dataset into input variables (X) and the response variable (y)
X = data[:, :-1]  # All columns except the last one
y = data[:, -1]  # Last column

# Variable names
variable_names = ['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4', 'Variable 5', 'Response']

# Create the model
model = Sequential()
model.add(Dense(8, input_dim=6, activation='relu'))  # Adjust the number of nodes and input_dim based on your preference
model.add(Dense(1, activation='linear'))  # Use 'linear' activation for regression tasks

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fit the model to the data
model.fit(X, y, epochs=100, batch_size=32)  # Adjust the number of epochs and batch_size based on your preference

# Make predictions
predictions = model.predict(X)

# Print the predictions with variable names
for i, prediction in enumerate(predictions):
    print("Prediction for variables", ', '.join(variable_names[:-1]), ":", prediction)

