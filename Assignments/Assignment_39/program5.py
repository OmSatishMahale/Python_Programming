import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def main():

    # Step 1: Load the dataset
    df = pd.read_csv("student_performance_ml.csv")

    #Step 2: Split the dataset into features and target variable
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    #Step 3 : Visualization
    plt.scatter(X["StudyHours"],
                Y,
                s=100,
                marker="o",
                alpha=0.8,
                edgecolors="black",
                linewidths=1,
                label="Students")

    plt.title("Marvellous Scatter Plot")
    plt.xlabel("Study Hours")
    plt.ylabel("Obtained Marks")
    plt.grid(True)

    plt.legend()
    plt.show()

    #Step 4: Split the dataset into training and testing sets
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    #Step 5: Create and train the Decision Tree Classifier model
    model = DecisionTreeClassifier()

    model = model.fit(X_train,Y_train)

    #Step 6: Make predictions on the test set
    Y_pred = model.predict(X_test)

    #Step 7: Evaluate the model's performance(Prediction)
    print("Values Predicted by Model is : ",Y_pred)

    print("Actual values is : ",Y_test)

    #Step 8: Calculate the accuracy of the model
    result = accuracy_score(Y_test,Y_pred)

    print("Accuracy of Model is : ",result * 100)

    #Step 9 : Confusion Matrix
    cm = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix:") 
    print(cm)

    print("Classification Report")
    print(classification_report(Y_test,Y_pred))

if __name__ == "__main__":
    main()