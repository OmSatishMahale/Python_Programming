import matplotlib.pyplot as plt

def main():

    language = ["C","C++","Java","Python"]
    students = [30,40,35,55]

    plt.bar(
        language,
        students,
        width = 0.6,                #Width of Bars
        edgecolor="black",          #border color of Bars
        linewidth=1,                #Width of bar Border
        alpha=0.8,                  #transperence 0.0 to 1.0 (Light blue Color)
        label="Students"            #Legend Text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of Students")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()