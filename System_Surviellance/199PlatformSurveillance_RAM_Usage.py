import psutil
import sys          
import os  
import time         
import schedule

def PlatformSurveillance(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as Directory is existing but it's not a Directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log File gets Successfully Created")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")
    print(f"Log Files gets Created Successfully {FileName}")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellous Platform Surveillance System ----\n")
    fobj.write("Log File gets Created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------ System Report --------------\n")

    #CPU Information
    fobj.write("Number of active CPU Cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    #RAM Information
    memory = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM Available : %s\n" %memory.total)
    fobj.write(Border+"\n")


    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("------------- End of Log File ------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance System ----")
    print(Border)

    #Handeling --h and --u
    if(len(sys.argv) == 2):
        if(len(sys.argv [1])== "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to perform")
            print("1 : It Fetch the Information of running processes")
            print("2 : It Fetch the Information about Primary Storage as RAM")
            print("3 : It Fetch the Information about Secondary Storage as HDD")
            print("4 : It Fetch the Information about Microprocessor")
            print("5 : It gets auto Scheduled Periodically")
            print("6 : It maintains all Record in Log File")
            print("7 : It Sends log files through mail Periodically")

        elif(len(sys.argv [1] )== "--u"  or sys.argv[1] == "--U"):
            print("Use the Automation Script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for Periodic Execution")
            print("Folder_Name : Name of Folder for the log file Creation")
            
        else:
            print("Unable to proceed as there is no matching Argument")
            print("Please use --h or --u for getting more Details")

    #Actual Project Code
    elif(len(sys.argv) == 3):

        #print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduler Started Successfully")
        print("Press Ctrl + c to abort the Automation Script")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurveillance, sys.argv[2])     
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of Arguments")
        print("Unable to Proceed as Arguments are not Matching")
        print("Please use --h or --u flag for getting more Details")

    print(Border)
    print("Thank you for using our Automation System")
    print(Border)

if __name__ == "__main__":
    main()