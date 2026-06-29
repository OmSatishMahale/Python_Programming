def CheckEven(No):
    return (No % 2 == 0)

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data))    #filter function only take the function which return  true or false
    print("Data After filter : ",FData)

if __name__ == "__main__":
    main()