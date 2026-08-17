import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def main():

    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    depths = [1,3,None]

    for depth in depths:

        model = DecisionTreeClassifier(max_depth=depth,random_state=42)

        model = model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        print(f"Max Depth : {depth} Accuracy of Model is : {accuracy_score(Y_test,Y_pred)*100}")

if __name__ == "__main__":
    main()

#Testing accuracy of model is same for different depth
