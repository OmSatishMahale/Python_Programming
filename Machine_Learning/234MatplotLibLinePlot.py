import matplotlib.pyplot as plt

def main():

    X = [1,2,3,4,5]
    Y = [10,25,18,35,30]

    plt.plot(
        X,
        Y,
        marker = "o",
        linestyle = "--",   
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Marvellous Line Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.grid(True)

    plt.legend()    #Show marks,student number 
    plt.show()      #Displays entire Graph on Screen

if __name__ == "__main__":
    main()