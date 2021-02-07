from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = loadtxt('Files/IndiansDiabetes.csv', delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# Create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='sigmoid'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit
model.fit(X, y, epochs=100, batch_size=10)

# Evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy:', (accuracy*100))

# Make probability predictions with the model
predictions = model.predict(X)
# round predictions 
rounded = [round(x[0]) for x in predictions]

predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(5):
	print(X[i].tolist(),'=>', predictions[i], ' (expected', y[i] ,')')
