#python ProcessSurveillance.py      2           MarvellousLog
#python ProcessSurveillance.py  time_interval    FolderName
#               0                   1               2
# len(sys.argv) -> 3


import psutil
import sys          #For taking Input from CMD
import os           #FOr File Related operations

def main():
    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance System ----")
    print(Border)

    #Handeling --h and --u
    if(len(sys.argv) == 2):
        if(len(sys.argv [1]) == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to perform")
            print("1 : It Fetch the Information of running processes")
            print("2 : It Fetch the Information about Primary Storage as RAM")
            print("3 : It Fetch the Information about Secondary Storage as HDD")
            print("4 : It Fetch the Information about Microprocessor")
            print("5 : It gets auto Scheduled Periodically")
            print("6 : It maintains all Record in Log File")
            print("7 : It Sends log files through mail Periodically")

        elif(len(sys.argv [1]) == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for Periodic Execution")
            print("Folder_Name : Name of Folder for the log file Creation")
            
        else:
            print("Unable to proceed as there is no matching Argument")
            print("Please use --h or --u for getting more Details")

    #Actual Project Code
    elif(len(sys.argv) == 3):
        pass
    else:
        print("Invalid number of Arguments")
        print("Unable to Proceed as Arguments are not Matching")
        print("Please use --h or --u flag for getting more Details")

    print(Border)
    print("Thank you for using our Automation System")
    print(Border)

if __name__ == "__main__":
    main()