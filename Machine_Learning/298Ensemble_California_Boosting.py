import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score

####################################################
#   Step 1 : Load the Data
####################################################
df = pd.read_csv("california_housing.csv")
print("Shape of Dataset is : ",df.shape)

print("First few records : ",df.head())

####################################################
#   Step 2 : Seperate Labels and features
####################################################

X = df.drop("target",axis = 1)
Y = df["target"]

print("Shape of X : ",X.shape)
print("SHape of Y : ",Y.shape)

####################################################
#   Step 3 : Split Dataset for training and testing
####################################################

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

####################################################
#   Step 4 : Create the boosting model
####################################################
model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
####################################################
#   Step 5 : Train the Model
####################################################
model = model.fit(X_train,Y_train)

####################################################
#   Step 6 : Test the Model
####################################################
Y_pred = model.predict(X_test)

####################################################
#   Step 7 : Evaluate the Model
####################################################
print("MSE : ",mean_squared_error(Y_test,Y_pred))
print("R2 : ",r2_score(Y_test,Y_pred))