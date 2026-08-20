import pandas as pd
import joblib

def LoadModel(Filename):
    model = joblib.load(Filename)

    print("Model Loaded Successfully")
    print(model.feature_names_in_)

    return model

def PredictPassenger(model):
    print("Enter the Information ")

    Pclass = int(input("Enter the Class (1/2/3) : "))
    Sex = int(input("Enter the Gender : (0 - Male / 1 - Female)"))
    Age = float(input("Enter the Age : "))
    sibsp = int(input("Enter Sibling and Spouse Count : "))
    Parch = int(input("Enter Parent and Child : "))
    Fare = int(input("ENter the Fare : "))
    Embarked = int(input("Enter Embark : "))

    passenger = pd.DataFrame([{
        "Pclass" : Pclass,
        "Sex" : Sex,
        "Age" : Age,
        "sibsp" : sibsp,
        "Parch" : Parch,
        "Fare" : Fare,
        "Embarked_1.0" : 1 if Embarked == 1 else 0,
        "Embarked_2.0" : 1 if Embarked == 2 else 0,
    }])

    passenger = passenger(model.feature_names_in_)

    result = model.predict(passenger)

    print(result)

def main():
    model = LoadModel("MarvellousTitanic.pkl")

    PredictPassenger(model)

if __name__ == "__main__":
    main()