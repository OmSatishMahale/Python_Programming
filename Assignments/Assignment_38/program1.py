import pandas as pd

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    print("First 5 entries from Dataset is : ")
    print(df.head())

    print("Last 5 Records of Dataset is : ")
    print(df.tail())

    #For getting dimension
    dimension = df.shape
    print("Dimensions : ",dimension)

    #For Getting number rows and COlumns Individually
    print("Number of rows in Dataset is : ",df.shape[0])
    print("Number of columns in Dataset is : ",df.shape[1])

    #For getting COlumns Names
    print("Column Names are : ",list(df.columns))

    print("Data Types of Each Column is : ",df.dtypes)

if __name__ == "__main__":
    main()