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

    #Approach A :- Using built in function
    print("Training Accuracy1 of model is : ",model.score(X_train,Y_train)*100)
    print("Testing Accuracy1 of Model is : ",model.score(X_test,Y_test)*100)

    #Approach B :- Using accuracy_score
    #Get Predictions first

    Y_train_pred = model.predict(X_train)
    Y_test_pred = model.predict(X_test)

    print("Training Accuracy2 is : ",accuracy_score(Y_train,Y_train_pred)*100)
    print("Testing Accuracy2 is : ",accuracy_score(Y_test,Y_test_pred)*100)

if __name__ == "__main__":
    main()


    #HEnce the model is Good fit

#3 Types of Fit

#1. Good Fit (Ideal)The Signal: Both training accuracy and testing 
#   accuracy are high, and the gap between them is very small.
#   Example: Training Accuracy: 95% | Testing Accuracy: 94%
#   Meaning: The model learned the true underlying patterns and 
#   generalizes perfectly to unseen data.
# 
# 2. Overfitting (High Variance) :-
#    The Signal: Training accuracy is high, but testing accuracy 
#    is significantly lower.
#    Example: Training Accuracy: 98% | Testing Accuracy: 75%
#    Meaning: The model memorized the training data 
#    (including its random noise) rather than learning the actual 
#    pattern. It performs terribly on new data.
# 
# 3. Underfitting (High Bias)
#   The Signal: Both training accuracy and testing accuracy are low.
#   Example: Training Accuracy: 55% | Testing Accuracy: 53%
#   Meaning: The model is too simple to learn the dataset's patterns. 
#   It performs poorly on both datasets
