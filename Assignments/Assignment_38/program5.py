import pandas as pd

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    summary = df.groupby("FinalResult")[["StudyHours","Attendance"]].mean()

    print(summary)
    
if __name__ == "__main__":
    main()
