import numpy as np

#Step 1 : Define input Features ie X
#                 [x1  x2  x3]
input = np.array([2.0,3.0,4.0])
print("X : ",input)

#Step 2 : Define Weights ie W
#                  [w1  w2  w3]
weights = np.array([0.5,0.3,0.2])
print("W : ",weights)

#Step 3 : Define bias ie b
#       b
bias = 1.0
print("b : ",bias)

#Step 4 : Calculate Weighted Sum ie Z
#z = w1x1 + w2x2 + w3x3 + b
#z = (0.5*2.0) + (0.3*3.0) + (0.2*4.0) + 1.0

z = np.dot(input,weights) + bias
print("z : ",z)

#Step 5 : Activation Function (ReLU - Rectified Linear Unit)
def ReLU(x):
    return max(0,x)

#Step 6 : Final Output
Y = ReLU(z)
print("Y : ",Y)