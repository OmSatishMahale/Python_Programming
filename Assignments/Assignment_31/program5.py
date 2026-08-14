# Write a program that accepts a directory name from the user and
# counts the number of files inside it every five minutes.
# Write the result into:
# DirectoryCountLog.txt
# Each entry should contain:
# • Directory path
# • Number of files
# • Date and time

import sys
import os
from datetime import datetime
import schedule
import time

def DirectoryScan(Directory):

    time = datetime.now()

    Ret = False

    Ret = os.path.exists(Directory)
    if(Ret == False):
        print("Directory does not exists")

    Ret = os.path.isdir(Directory)
    if(Ret == False):
        print("The entered I/P is not a Directory")
    
    fobj = open("Marvellous.txt","a")

    fCount = 0

    for FolderName, SubFolder, FileName in os.walk(Directory):
        for fname in FileName:
            fCount = fCount + 1

    fobj.write("Total file Count is : "+str(fCount)+"\n")
    fobj.write("Files get Scanned at : "+time.strftime("%d-%m-%Y %I:%M:%S %p")+"\n")

    fobj.close()


def main():

    if(len(sys.argv) == 2):
        schedule.every(10).seconds.do(DirectoryScan,sys.argv[1])
        
        while(True):
                schedule.run_pending()
                time.sleep(1)

if __name__ == "__main__":
    main()