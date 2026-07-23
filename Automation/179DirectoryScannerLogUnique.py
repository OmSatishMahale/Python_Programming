import sys       
import os     
import time               

def DirectoryScanner(DirectoryPath):
    
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    print("Log File gets Created with Name : ",LogFileName)

    fobj = open(LogFileName,"w")
    fobj.write("Marvellous Automation Script \n")
    fobj.write("Files from the Directory are : \n")

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")

    fobj.close()

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1]=="--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to travel the Directory")
            print("For Better usage please check --u flag")

        elif(sys.argv[1]=="--u" or sys.argv[1] == "--U"):
            print("Please Execute the Script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be Absolute Path")

        else:
            DirectoryScanner(sys.argv[1])
    
    else:
        print("Invalid Numbers of Arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank You for using Marvellous Automation Script")
    print(Border)

if __name__ =="__main__":
    main()