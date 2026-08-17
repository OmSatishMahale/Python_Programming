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

    model_before = DecisionTreeClassifier(random_state=42)

    model_before = model_before.fit(X_train,Y_train)

    Y_pred_before = model_before.predict(X_test)
    accuracy_before = accuracy_score(Y_test, Y_pred_before)
    print("Accuracy before dropping SleepHours:", accuracy_before * 100)

    model_after = DecisionTreeClassifier(random_state=42)

    X_after = df.drop(columns=["SleepHours", "FinalResult"])
    Y_after = df["FinalResult"]

    X_train_after, X_test_after, Y_train_after, Y_test_after = train_test_split(
        X_after, Y_after, test_size=0.5, random_state=42
    )

    model_after = model_after.fit(X_train_after, Y_train_after)
    Y_pred_after = model_after.predict(X_test_after)
    accuracy_after = accuracy_score(Y_test_after, Y_pred_after)

    print("Accuracy of Model after dropping SleepHours:", accuracy_after * 100)

    diff = accuracy_after - accuracy_before

    if diff > 0:
        print("Accuracy improved by:", diff * 100, "%")
    elif diff < 0:
        print("Accuracy dropped by:", abs(diff) * 100, "%")
    else:
        print("No change in accuracy")
if __name__ == "__main__":
    main()