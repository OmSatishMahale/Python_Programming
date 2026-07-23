import sys                  

def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1]=="--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to travel the Directory")
            print("For Better usage please check --u flag")

        elif(sys.argv[1]=="--u" or sys.argv[1] == "--U"):
            print("Please Execute the Script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be Absolute Path")

        else:
            DirectoryName = sys.argv[1]
            print("Directory name is : ",DirectoryName)
    else:
        print("Invalid Numbers of Arguments")
        print("Please use --h or --u for more information")

if __name__ =="__main__":
    main()