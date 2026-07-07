#Write a program which print the following pattern 

#       *   *   *   *   *
#       *   *   *   *   *
#       *   *   *   *   *
#       *   *   *   *   *
#       *   *   *   *   *

def Pattern(Row,Col):
    
    for i in range(Row):
        for j in range(Col):
            print("*",end="\t")
        print()


def main():
    
    Value1 = int(input("Enter number of Rows : "))
    Value2 = int(input("Enter number of column : "))

    Pattern(Value1,Value2)

if __name__ == "__main__":
    main()