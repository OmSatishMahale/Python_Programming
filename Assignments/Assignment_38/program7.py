import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    sns.scatterplot(
        data=df,
        x="StudyHours",
        y="PreviousScore",
        hue = df["PreviousScore"] < 55,
        palette={True:"red",False:"green"},
        s=100,
        marker="o",
        alpha=0.8,
        linewidths=0.9
    )
    
    plt.title("Study Performance")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")

    plt.grid()
    plt.legend(title="Status",labels=["Pass","Fail"])
    plt.axhline(y=55,color="black",linestyle="--",alpha=0.5)
    plt.show()
    
if __name__ == "__main__":
    main()
