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

    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of the model:", accuracy * 100, "%")

    important = []
    non_important = []

    for name, score in zip(X.columns, model.feature_importances_):
        print(f"Feature: {name}, Score: {score}")
        
        if score > 0.1:  
            important.append(name)
        else:
            non_important.append(name)

    print("Important features:", important)

    print("Non-important features:", non_important)

if __name__ == "__main__":
    main()