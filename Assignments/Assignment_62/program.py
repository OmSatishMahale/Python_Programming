import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

###################################################
#   Step 1 : Load the Data
###################################################
print("Step 1 : Load the Data")

data = pd.read_csv("Employee_Attrition.csv")
print("Dataset Loaded Successfully")

print("------------------------------------------------------")

###################################################
#   Step 2 : Display Shape,columns and first five Records
###################################################
print("Step 2 : Display Shape,columns and first five Records")

print("SHape of Dataset is : ")
print(data.shape)

print("Columns from Dataset is : ")
print(data.columns)

print("FIrst 5 records from Dataset is : ")
print(data.head())

print("------------------------------------------------------")
###################################################
#   Step 3 : Check for missing Values
###################################################
print("Step 3 : Check for missing Values")
missing_values = data.isnull().sum()
print("Total missing Values from Dataset is : ")
print(missing_values)

print("------------------------------------------------------")

###################################################
#   Step 4 : Identify numerical and categorical Variables
###################################################
print("Step 3 : Identify numerical and categorical Variables")

numerical_cols = data.select_dtypes(include=[np.number]).columns.tolist()
print("Numerical Features from Dataset is : ")
print(numerical_cols)

categorical_cols = data.select_dtypes(exclude=[np.number]).columns.tolist()
print("Categorical Features from Dataset is : ")
print(categorical_cols)

print("------------------------------------------------------")

###################################################
#   Step 5 and 6 : Convert Categorical Features into Numeric
###################################################
print("Step 5 and 6: Convert Categorical Features into Numeric")

binary_mapping = {"Yes":1,"No":0}

data["OverTime"] = data["OverTime"].map(binary_mapping)
data["Attrition"] = data["Attrition"].map(binary_mapping)

print(data[["OverTime","Attrition"]].head())
print("------------------------------------------------------")

###################################################
#   Step 7 : Seperate Independent and Dependent Variables
###################################################
print("Step 7 : Seperate Independent and Dependent Variables")
X = data[['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears', 'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance', 'NumCompaniesWorked', 'TrainingTimesLastYear','OverTime']]
Y = data['Attrition']

print("Independent Variables are : ")
print(X.head())

print("Dependent Variables are : ")
print(Y.head())

print("------------------------------------------------------")

###################################################
#   Step 8 : Divide the Dataset for Training and Testing
###################################################
print("Step 8 : Divide the Dataset for Training and Testing")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Shape of Training Input (X_train) : ")
print(X_train.shape)

print("Shape of Testing Input (X_test) : ")
print(X_test.shape)

print("SHape of Training Output (Y_train) : ")
print(Y_train.shape)

print("SHape of Testing Output (Y_test) : ")
print(Y_test.shape)
print("------------------------------------------------------")
###################################################
#   Step 9 : Apply appropriate feature Scaling
###################################################
print("Step 9 : Apply appropriate feature Scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

print("Scaled Training Data is : ")
print(X_train_scaled[:5])
print("------------------------------------------------------")

###################################################
#   Step 10 : Design an MLP with atleast two Hidden Layers
###################################################
print("Step 10 : Design an MLP with atleast two Hidden Layers")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)
print("------------------------------------------------------")
###################################################
#   Step 11 : Train the Network
###################################################
print("Step 11 : Train the Network")

model.fit(X_train_scaled,Y_train)

Y_pred = model.predict(X_test_scaled)
###################################################
#   Step 12 : Loops taken to train the Network
###################################################
loops = model.n_iter_
print("Loops taken to Train the Network : ",loops)

###################################################
#   Step 13 : Calculate the Training Accuracy
###################################################
accuracy = accuracy_score(Y_test,Y_pred)
print("Training Accuracy of Model is : ",accuracy*100)

###################################################
#   Step 15 : Confusion Matrix
###################################################
cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix : ")
print(cm)

###################################################
#   Step 17 : Function PredictAttrition
###################################################

employee_data = pd.DataFrame([
                            [23,12345,1,1,12,5,2,0,0,1],
                            [24,14345,1,1,12,5,2,0,0,0],
                            [25,16345,1,1,12,5,2,0,0,0],
                            [34,108345,11,11,43,2,1,0,0,1],
                            [28,21345,1,1,12,5,2,0,0,1],
                              ],
                            columns=['Age', 'MonthlyIncome', 
                                     'YearsAtCompany', 
                                     'TotalWorkingYears', 
                                     'DistanceFromHome', 
                                     'JobSatisfaction', 
                                     'WorkLifeBalance', 
                                     'NumCompaniesWorked', 
                                     'TrainingTimesLastYear',
                                     'OverTime'])

employee_data_scaled = scalar.transform(employee_data)

###################################################
#   Step 18 : Testing the Model with New Employee Data
###################################################
def PredictAttrition(employee_data_scaled):
    prediction = model.predict(employee_data_scaled)
    return prediction

new_prediction = PredictAttrition(employee_data_scaled)
print("Predicted Attrition for New Employees is : ")
print(new_prediction)