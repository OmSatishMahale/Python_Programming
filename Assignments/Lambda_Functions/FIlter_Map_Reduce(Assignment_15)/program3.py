#Write a lambda function using filter() which accept list of numbers and return list of Odd numbers

Odd = lambda No : (No % 2 != 0)

def main():
    Data = list()
    Size = int(input("Enter the size of list : "))

    print("Enter the elements of list : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    FData = list(filter(Odd,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()