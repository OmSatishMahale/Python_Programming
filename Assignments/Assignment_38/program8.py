import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    plt.figure(figsize=(6, 6))

    sns.boxplot(
        y=df["Attendance"], 
        color="skyblue", 
        flierprops={"markerfacecolor": "red", "marker": "D", "markersize": 8}
    )
    
    plt.title("Attendance Distribution & Outliers")
    plt.ylabel("Attendance Rate")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

if __name__ == "__main__":
    main()
