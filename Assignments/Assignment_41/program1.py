import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def KNNWinePredictor(DataPath):

    #Step 1 : Load the data
    df = pd.read_csv(DataPath)

    #STep 2 : Clean the Data

    df.dropna(inplace=True)

    print("Shape of DataSet is : ",df.shape)
    print("Shape of Records : ",df.shape[0])
    print("Shape of Columns : ",df.shape[1])

    #Step 3 : Seperate Dependent and Independent Variables

    X = df.drop(columns="Class")
    Y = df["Class"]

    print("Shape of X is : ",X.shape)
    print("Shape of Y is : ",Y.shape)

    #Step 4 : Split the Data for Training and Testing Purpose

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    print("Details of Training and Testing Data : ")

    print("SHape of X_train : ",X_train.shape)
    print("SHape of Y_train : ",Y_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_test : ",Y_test.shape)

    #Step 5 : Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    #Step 6 : HyperTuning and Model Training

    accuracy_scores = []

    k_value = range(1,21)

    for k in k_value:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_pred,Y_test)
        accuracy_scores.append(accuracy)

    for value,no in zip(k_value,accuracy_scores):
        print(f"K : {value},Accuracy : {no}")

def main():
    KNNWinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()