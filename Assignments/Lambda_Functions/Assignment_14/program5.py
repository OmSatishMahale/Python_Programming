EvenOdd = lambda No : (No % 2 == 0)

def main():

    Value = int(input("Enter the number : "))
    Ret = EvenOdd(Value)
    if(Ret == True):
        print(Ret)
    else:
        print(Ret)

if __name__ == "__main__":
    main()