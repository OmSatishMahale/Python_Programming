import pandas as pd
import matplotlib.pyplot as plt

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    plt.hist(
        df["StudyHours"],
        bins=5,
        edgecolor="Black",
        alpha=0.8,
        rwidth=0.9
    )

    plt.title("Study Performance")
    plt.xlabel("Study Hours")
    plt.ylabel("Frequency")

    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()
