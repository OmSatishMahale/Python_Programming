#Write a program which print 

#       *   *   *   *   *
#       *   *   *   *
#       *   *   *
#       *   *
#       *

def Pattern(Row,Col):

    for i in range(1,Row+1):
        for j in range(1,Col+1):
            if(i >= j):
                print(j,end="\t")
        print()

def main():
    Value1 = int(input("Enter number of rows : "))
    Value2 = int(input("Enter number of Column : "))

    Pattern(Value1,Value2)

if __name__ == "__main__":
    main()