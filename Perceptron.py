import numpy as np
import matplotlib.pyplot as plt

# Training data for AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

# #Training data y=f(x)=2x+3
# X = np.array([[1],[2],[3],[4],[5]])
# y = np.array([5,7,9,11,13])

def step(x,th):
  if x>=th:
    return(1)
  return(0)

def linearInt(x):
  return (round(x))

def predict(X, y, weights):
  print("X\tActual\tPredicted")
  for x_input, y_output in zip(X, y):
    inSum=np.sum(x_input * weights)
    y_pred = step(inSum,th)
    print(x_input,"\t",y_output,"\t",y_pred)

# initialize constants
lr = 0.1
th = 0.5

# Initialize weights array
weights = []

# Loop through each element in X
for i in range(X.shape[1]): #+1 for te bias
    # Initialize w randomly between 0 and 1 using Python's random module & Convert w to have only one digit after the decimal point
    w = round(np.random.rand(),1)
    weights.append(w)

print("Randomly initialized weights for each input:")
for i in range(len(weights)):
    print(f"weights[{i}]:", weights[i])
    
# initialize constants
lr = 0.1
th = 0.5

# Initialize weights array
weights = []

# Loop through each element in X
for i in range(X.shape[1]): #+1 for te bias
    # Initialize w randomly between 0 and 1 using Python's random module & Convert w to have only one digit after the decimal point
    w = round(np.random.rand(),1)
    weights.append(w)

print("Randomly initialized weights for each input:")
for i in range(len(weights)):
    print(f"weights[{i}]:", weights[i])
    
import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)

#For AND/OR Logic Gates
# print (step(0.5,th))
iterateFlag = True
while (iterateFlag):
  iterateFlag = False
  for x_input, y_output in zip(X, y):
    inSum=np.sum(x_input * weights)
    y_pred = step(inSum,th)
    err = y_output - y_pred
    if(err!=0):
      iterateFlag = True
      for i in range(len(weights)):
        dw = lr * x_input[i] * err
        weights[i] = weights[i] + dw
      print("input:",x_input, "actual output:",y_output,"predicted output: ",y_pred,"updated weights:", weights)

print("Final weights:", weights)

# for y=f(x)=2x+3

iterateFlag = True
# Lists to store MSE values and epoch numbers
mse_values = []
epochs = []
epoch_count = 0

while (iterateFlag):
  epoch_count += 1
  squared_errors = []
  iterateFlag = False

  for x_input, y_output in zip(X, y):
    inSum = np.sum(x_input * weights)
    inSum += 1 * weights[len(weights)-1]
    # y_pred = step(inSum,th)
    y_pred = linearInt(inSum)
    err = y_output - y_pred
    squared_errors.append(err**2)
    if(err!=0):
      iterateFlag = True
      for i in range(len(weights)-1):
        dw = lr * x_input[i] * err
        weights[i] = weights[i] + dw
      weights[len(weights)-1] += lr * np.sum(err)
      print("input:",x_input, "actual output:",y_output,"predicted output: ",y_pred,"updated weights:", weights)
  mse = np.mean(squared_errors)
  mse_values.append(mse)
  epochs.append(epoch_count)
print("Final weights:", weights)


# Plot MSE vs. Epochs
plt.figure(figsize=(20, 6))  # Set figure size wider
plt.plot(epochs, mse_values, marker='o', linestyle='None', color='blue')  # Plot MSE values as dots
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs. Epochs')
plt.grid(True)  # Add grid
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Mean Squared Error (MSE)
def calculate_mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([5, 7, 9, 11, 13])

# Initialize weights
weights = np.array([0.1, 0.3])

# Learning rate
lr = 0.01

# Threshold
th = 0.5

# Activation function (linear)
def linearInt(x):
    return x

# Lists to store MSE values and epoch numbers
mse_values = []
epochs = []
epoch_count = 0

# Training loop
iterateFlag = True
while iterateFlag:
    epoch_count += 1
    squared_errors = []
    iterateFlag = False

    for x_input, y_output in zip(X, y):
        inSum = np.sum(x_input * weights)
        inSum += 1 * weights[-1]
        y_pred = linearInt(inSum)
        err = y_output - y_pred
        squared_errors.append(err**2)
        if err != 0:
            iterateFlag = True
            for i in range(len(weights)-1):
                dw = lr * x_input[i] * err
                weights[i] = round(weights[i] + dw, 3)  # Round to 3 decimal points
            weights[-1] = round(weights[-1] + lr * np.sum(err), 3)  # Round to 3 decimal points
            print("input:", x_input, "actual output:", y_output, "predicted output:", y_pred, "updated weights:", weights)
    mse = np.mean(squared_errors)
    mse_values.append(mse)
    epochs.append(epoch_count)

print("Final weights:", weights)

# Plot MSE vs. Epochs
plt.plot(epochs, mse_values)
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs. Epochs')
plt.show()



predictFx(X,y,weights)