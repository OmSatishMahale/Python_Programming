import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def main():

    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = DecisionTreeClassifier()

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("Values Predicted by Model is : ",Y_pred)

    print("Actual values is : ",Y_test)

    result = accuracy_score(Y_test,Y_pred)

    print("Accuracy of Model is : ",result * 100)

    cm = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix:")
    print(cm)

if __name__ == "__main__":
    main()