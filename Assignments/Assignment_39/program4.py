import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


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

#############################################################
#
#   Predict whether student will pass or fail
#
#############################################################

    feature_cols = {
        "StudyHours":6,
        "Attendance":85,
        "PreviousScore":66,
        "AssignmentsCompleted":7,
        "SleepHours":7
        }

    X1 = pd.DataFrame([feature_cols])

    pred = model.predict(X1)

    pred = "pass" if pred == 1 else "fail"
    print("Student will : ",pred)
    
if __name__ == "__main__":
    main()