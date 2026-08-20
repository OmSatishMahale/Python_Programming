import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Step 1 : Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables X : ",X)
    print("Values of Dependent Variables Y : ",Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean_X is : ",mean_x)
    print("Mean_Y is : ",mean_y)

    n = len(X)  #5

    numerator = 0
    denominator = 0

    #Calculate Slope
    # m = sum(X-Xbar) * (Y-Ybar) / Sum(X-Xbar) ** 2
    for i in range(n):
        numerator = numerator + ((X[i] - mean_x)*(Y[i]-mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator
    print("Slope of line m is : ",m)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()