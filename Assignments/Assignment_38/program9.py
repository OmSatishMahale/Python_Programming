import matplotlib.pyplot as plt
import pandas as pd

def main():

    df = pd.read_csv("student_performance_ml.csv")

    plt.scatter(
    x=df["AssignmentsCompleted"],
    y=df["FinalResult"],
    alpha=0.7,
    edgecolors="black",
    color="orange",
    label="Students"
)

    plt.title("Marvellous Scatter Plot")
    plt.xlabel("Assignment Completed")
    plt.ylabel("Final Result")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()