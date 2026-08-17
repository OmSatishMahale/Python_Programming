import pandas as pd

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    print("Average StudyHours of Students is : ",df["StudyHours"].mean())
    print("Average Attendance of Students is : ",df["Attendance"].mean())
    print("Maximum Previous Score of Student is : ",df["PreviousScore"].max())
    print("Minimum Previous Sleep Hour of Student is : ",df["SleepHours"].min())

    
if __name__ == "__main__":
    main()