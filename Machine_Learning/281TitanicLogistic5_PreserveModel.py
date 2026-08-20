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

#Step 3 : Split Data
#------------------------------------------------------------
#
#   Function Name : SplitData
#   Description : It Perform Splitting Activity
#   IP : Data Frame
#   OP : 4 Subset for Training and Testing
#   Author : Om Satish Mahale
#   Date : 16/8/2025
#
#------------------------------------------------------------
def SplitData(df):
    X = df.drop("Survived",axis= 1)
    Y = df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("DataSet Splitting completed Successfully")

    return X_train,X_test,Y_train,Y_test

#Step 4 : Train Model
#------------------------------------------------------------
#
#   Function Name : TrainModel
#   Description : Model Training
#   IP : Training Features
#   OP : Trained Model
#   Author : Om Satish Mahale
#   Date : 16/8/2026
#
#------------------------------------------------------------
def TrainModel(X_train,Y_train):
    model = LogisticRegression(max_iter=1000)
    model = model.fit(X_train,Y_train)
    print("Model Trained Successfully")

    return model

#Step 5 : Model Testing
#------------------------------------------------------------
#
#   Function Name : EvaluateModel
#   Description : It perform Model Testing
#   IP : model, testing data(Features,label)
#   OP : None
#   Author : Om Satish Mahale
#   Date : 16/8/2026
#
#------------------------------------------------------------
def EvaluateModel(model,X_test,Y_test):

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of Model is : ",accuracy)

    print("Confusion Matrix")
    print(confusion_matrix(Y_test,Y_pred))

#------------------------------------------------------------
#
#   Function Name : main
#   Description : Entry Point Function
#   IP : None
#   OP : None
#   Author : Om Satish Mahale
#
#------------------------------------------------------------

#Step 6 : Preserve Model
#------------------------------------------------------------
#
#   Function Name : PreserveModel
#   Description : It perform Model Preservation
#   IP : model
#   OP : None
#   Author : Om Satish Mahale
#   Date : 16/8/2026
#
#------------------------------------------------------------
def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model Preserved with name : ",filename)

def main():

    #Step 1
    df = LoadData("MarvellousTitanicDataset.csv")

    #Step 2
    df = PreprocessData(df)

    #Step 3 
    X_train,X_test,Y_train,Y_test = SplitData(df)

    #Step 4 
    model = TrainModel(X_train,Y_train)

    #Step 5
    EvaluateModel(model,X_test,Y_test)

    #Step 6
    PreserveModel(model,"MarvellousTitanic.pkl")
    
if __name__ == "__main__":
    main()