import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def main():

    Data = {
        "StudyHours" :[3,4,6,1,2], 
        "Attendance" :[65,80,90,50,70],
        "PreviousScore":[85,43,90,40,75],
        "AssignmentsCompleted":[3,7,5,2,4],
        "SleepHours":[7,6,8,5,6],
        "FinalResult":["Pass","Fail","Pass","Fail","Pass"]
    }
    dobj = pd.DataFrame(Data)

    X = dobj.drop(columns=["FinalResult"])
    Y = dobj["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = DecisionTreeClassifier(random_state=42)

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("Expected Answer : ",list(Y_test))
    print("Predicted Answer : ",list(Y_pred))

    print("Accuracy of Model is (Built-in): ",accuracy_score(Y_test,Y_pred)*100)

    miss_count = 0

    Y_actual = list(Y_test)

    for i in range(len(Y_actual)):
        if Y_actual[i] != Y_pred[i]:
            
            miss_count += 1
        row = X_test.iloc[i].to_dict()

    print("Misclassified STudents : ",row)
    print("COunt of Misclassified STudents : ",miss_count)

if __name__ == "__main__":
    main()