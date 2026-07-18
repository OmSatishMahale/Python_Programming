#Write a lambda function using filter which accept list and return count of even number from list

CountEven = lambda No : No % 2 == 0

def main():
    Data = list()
    Size = int(input("Enter the size of list : "))

    print("ENter the elements of list : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    FData = list(filter(CountEven,Data))
    print("Count of even numbers is : ",len(FData))

if __name__ == "__main__":
    main()