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
#   Date : 16/8/2026
#
#------------------------------------------------------------
def LoadData(filename):

    df = pd.read_csv(filename)
    print("Data Set Loaded Successfully")
    print(df.head())

    return df

#Step 2 : Data PreProcess
#------------------------------------------------------------
#
#   Function Name : PreprocessData
#   Description : It Perform Data Analysis
#   IP : Data Frame
#   OP : Updated Data Fram
#   Author : Om Satish Mahale
#   Date : 16/8/2025
#
#------------------------------------------------------------
def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors="ignore")

    #Handel Missing Values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert Categorical to numeric data
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )
    print(df.head())
    print("Data Preprocessing Completed")
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

    #Step 1
    df = LoadData("MarvellousTitanicDataset.csv")

    #Step 2
    df = PreprocessData(df)

if __name__ == "__main__":
    main()