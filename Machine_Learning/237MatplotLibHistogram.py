import matplotlib.pyplot as plt

def main():

    marks = [45,55,60,62,65,67,70,72,75,78,80,82,85,90,92]

    plt.hist(
        marks,                  #Continous Data
        bins= 5,                #Number of Groups
        edgecolor="black",      #Border Color
        alpha=0.8,              #transperency
        rwidth=0.9              #relative width of bars
    )
    plt.title("Marvellous Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()