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

    model = DecisionTreeClassifier(max_depth=None, random_state=42)
    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    Y_pred_train = model.predict(X_train)

    accuracy_testing = accuracy_score(Y_test, Y_pred)
    accuracy_training = accuracy_score(Y_train, Y_pred_train)
    
    print("Testing Accuracy of the model:", accuracy_testing * 100, "%")
    print("Training Accuracy of the model:", accuracy_training * 100, "%")

if __name__ == "__main__":
    main()