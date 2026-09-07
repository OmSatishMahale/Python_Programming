##################################################
#   Deep Learning Pipeline
###################################################
#   1. Read the Data from CSV
#   2. Data Analysis(EDA)
#   3. Preprocessing
#   4. Train Test Split
#   5. Feature Scaling
#   6. FNN Model Training
#   7. Model Evaluation
#   8. Graphical Representation
#   9. Model Preserve
#   10. Model loading and Preserve
#   11. Test unseen Data
##################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

##################################################
#   Step 1 : Read the Data from CSV
##################################################
print("Step 1 : Read the Data from CSV")

data = pd.read_csv("placement_data.csv")

print("Complete Dataset : ")
print(data)

##################################################
#   Step 2 : Data Analysis(EDA)
##################################################
print("Step 2 : Data Analysis (EDA)")
print("First few Entries")
print(data.head())

print("Column names : ")
print(data.columns)

print("Shape of Dataset : ")
print(data.shape)

print("Statistical Summary : ")
print(data.describe)

##################################################
#   Step 3 : Preprocessing
##################################################
print("Step 3 : Preprocessing")

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data["Placed"]

print("Input Features : ")
print(X.head())

print("Target : ")
print(Y.head())

##################################################
#   Step 4 : Train Test Split
##################################################
print("Step 4 : Train Test Split")
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.30,random_state=42)

print("Shape of Training Input (X_train) : ")
print(X_train.shape)

print("Shape of Testing Input (X_test) : ")
print(X_test.shape)

print("Shape of Training Output (Y_train) : ")
print(Y_train.shape)

print("Shape of Testing Output (Y_test) : ")
print(Y_test.shape)

##################################################
#   Step 5 : Feature Scaling
##################################################
print("Step 5 : Feature Scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print("Scaled Training Data : ")
print(X_train_scaled[:5])

##################################################
#   Step 6 : FNN Model Training
##################################################
print("Step 6 : FNN Model Training")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)
print(model)
print("Train the Model")
model.fit(X_train_scaled,Y_train)
print("Model Training Completed")

##################################################
#   Step 7 : Model Evaluation
##################################################
print("Step 7 : Model Evaluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_pred,Y_test)
print("Accuracy : ",accuracy)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix : ")
print(cm)

print("Predict the probability : ")
Y_prob = model.predict_proba(X_test_scaled)
print(Y_prob[:5])

##################################################
#   Step 8 : Graphical Representation
##################################################
#At home

##################################################
#   Step 9 : Model Preserve
##################################################
print("Step 9 : Model Preserve")
joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scalar,"placement_scalar.pkl")

print("Model and Scalar gets Dump Successfully")

##################################################
#   Step 10 : Model loading and Preserve
##################################################
print("Step 10 : Model loading and Preserve")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scalar = joblib.load("placement_scalar.pkl")

print("Model gets Loaded Successfully")

##################################################
#   Step 11 : Test Unseen Data
#   Aptitude :          70
#   Coding :            75
#   Communications :    80
#   Academics :         85
#   Internship :        1
##################################################

new_student = pd.DataFrame([[70,75,80,85,1]],columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)
new_probability = loaded_model.predict_proba(new_student_scaled)

print("New Student Data :")
print(new_student)

print("Prediction Probability : ",new_probability)

if new_prediction[0] == 1:
    print("Prediction : Placed")
else:
    print("Prediction : Not Placed")