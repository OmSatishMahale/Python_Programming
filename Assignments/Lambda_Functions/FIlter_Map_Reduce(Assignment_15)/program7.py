#Write a lambda function using filter which accept list of string and return list of string having length greater than 5

leng = lambda val : len(val)>5

def main():
    Data = list()
    Size = int(input("Enter size of list : "))

    print("Enter the String for list : ")

    for i in range(Size):
        str = input()
        Data.append(str)

    FData = list(filter(len,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()