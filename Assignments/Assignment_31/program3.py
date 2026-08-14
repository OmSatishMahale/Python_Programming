# Write a program that scans a specified directory every minute.
# The task should display:
# • Directory name
# • Number of files
# • Number of subdirectories
# • Date and time of scanning
# Use the os module.
# Example output:
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan Time: 25-07-2026 04:30:00 PM

import sys
import os
from datetime import datetime

def DirectoryScan(Directory):

    time = datetime.now()

    Ret = False

    Ret = os.path.exists(Directory)
    if(Ret == False):
        print("Directory does not exists")

    Ret = os.path.isdir(Directory)
    if(Ret == False):
        print("The entered I/P is not a Directory")
    
    fobj = open("Marvellous.txt","w")

    SubfCount = 0
    fCount = 0

    for FolderName, SubFolder, FileName in os.walk(Directory):
        for fname in FileName:
            fCount = fCount + 1

        for subf in SubFolder:
            SubfCount = SubfCount + 1

    fobj.write("Total file Count is : "+str(fCount)+"\n")
    fobj.write("Total Subfolder is : "+str(SubfCount)+"\n")
    fobj.write("Files get Scanned at : "+time.strftime("%d-%m-%Y %I:%M:%S %p")+"\n")

    fobj.close()


def main():

    if(len(sys.argv) == 2):
        DirectoryScan(sys.argv[1])

if __name__ == "__main__":
    main()