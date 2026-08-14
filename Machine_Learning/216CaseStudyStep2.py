import pandas as pd

Border = "-"*30
####################################################
#   Step 1 : Load the DataSet
####################################################

print(Border)
print("Step 1 : Load the DataSet")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)      #df = DataFrame (2D array)

print("Dataset Loaded Successfully ")
print("Initial Entries from Dataset are : ")
print(df.head())


###############################################################
#   Step 2 : Data Analysis  (EDA - Exploratory Data Analysis)
###############################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing values per Column : ")
print(df.isnull().sum())

print("Class Distribution (Species Count) ")
print(df["species"].value_counts())

print("Statistical report of Dataset : ")
print(df.describe())