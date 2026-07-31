# Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

import sys
import os

def CopyContents(ExistingFile,NewFile):

    Ret = False
    Ret = os.path.exists(ExistingFile)

    if(Ret == False):
        print("File Does not exists")
        return

    fobj1 = open(ExistingFile,"r")
    fobj2 = open(NewFile,"w")

    for line in fobj1:
        fobj2.write(line)

    fobj1.close()
    fobj2.close()

def main():

    if(len(sys.argv) == 3):
        CopyContents(sys.argv[1],sys.argv[2])
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()