#Write a program which print 

#       *   *   *   *   *
#       *   *   *   *
#       *   *   *
#       *   *
#       *

def Pattern(Row,Col):

    for i in range(Row):
        for j in range(Col):
            if(i <= j):
                print("*",end="\t")
        print()

def main():
    Value1 = int(input("Enter number of rows : "))
    Value2 = int(input("Enter number of Column : "))

    Pattern(Value1,Value2)

if __name__ == "__main__":
    main()