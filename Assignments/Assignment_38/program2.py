import pandas as pd

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    print("Total Number of students from CSV is : ",len(df))

    counts = df["FinalResult"].value_counts()
    print("Total number of students passed is : ",counts[1])
    print("Total number of students failed is : ",counts[0])

    
if __name__ == "__main__":
    main()