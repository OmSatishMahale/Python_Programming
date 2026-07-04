#Write a lambda function using filter,which accept list from user and print the list of number divisible by 3 and 5

Divisible = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    Data = list()

    Size = int(input("ENter the size of list : "))

    print("Enter the elements of list : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    FData = list(filter(Divisible,Data))  
    print("Data after filter is : ",FData)  

if __name__ == "__main__":
    main()