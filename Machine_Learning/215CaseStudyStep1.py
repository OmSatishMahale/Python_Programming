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