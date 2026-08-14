import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    Border = "-"*40

    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print(Border)
    print("Some entries from dataset : ")
    print(df.head())
    print(Border)

    #Step 2 : Clean the Dataset

    print(Border)
    print("Step 2 : CLean the Dataset")
    print(Border)

    df.dropna(inplace=True)

    print("Shape of Dataset : ",df.shape)
    print("Total Records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])

    print(Border)

    #Step 3 : Seperate Independent and Dependent Variable

    print(Border)
    print("Step 3 : Seperate Independent and Dependent Variable")
    print(Border)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("SHape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input Columns : ",X.columns.tolist())
    print("Output Columns : Class")
    print(Border)

    #Step 4 - Split the Data for Training and Testing Purpose
    print(Border)
    print("Step 4 : Split the Data for Training and Testing Purpose")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    print(Border)

    print("Details of Training and Testing Data : ")

    print("SHape of X_train : ",X_train.shape)
    print("SHape of X_test : ",X_test.shape)

    print("SHape of Y_train : ",Y_train.shape)
    print("SHape of Y_test : ",Y_test.shape)
    print(Border)

    #Step 5 : Feature Scaling

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature Scaling Done")
    print(Border)

    #Step 6 : Hyperparameter Tuning

    accuracy_scores = []

    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)
    print("Acuuracy Report : ")

    for no in accuracy_scores:
        print(no)

    print(Border)

    print(Border)
    print("Graphical Representation")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker="o")
    plt.title("K values vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Value of Accuracy")

    plt.grid(True)
    plt.xticks(list(K_values))

    plt.show()
    
def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ =="__main__":
    main()