#Write a program which accept marks and display Grades

def Grade(Marks):
    
    if(Marks >= 75):
        print("Distinction")
    elif(Marks >= 60):
        print("First Class")
    elif(Marks >= 50):
        print("Second Class")
    else:
        print("Fail")
        
def main():
    
    Value = int(input("Enter Marks : "))
    Grade(Value)

if __name__ == "__main__":
    main()