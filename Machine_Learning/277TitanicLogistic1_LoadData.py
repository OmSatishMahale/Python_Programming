import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#Step 1 : Load Data

#------------------------------------------------------------
#
#   Function Name : LoadData
#   Description : Load the Data from csv
#   IP : Name of CSV
#   OP : Data Fram
#   Author : Om Satish Mahale
#
#------------------------------------------------------------

def LoadData(filename):

    df = pd.read_csv(filename)
    print("Data Set Loaded Successfully")
    print(df.head())

    return df


#------------------------------------------------------------
#
#   Function Name : main
#   Description : Entry Point Function
#   IP : None
#   OP : None
#   Author : Om Satish Mahale
#
#------------------------------------------------------------

def main():

    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()