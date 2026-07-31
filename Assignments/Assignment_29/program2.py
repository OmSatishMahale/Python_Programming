# Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.

import sys
import os

def CountWords(FileName):

    Ret = False
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("File Does not exists")
        return

    fobj = open(FileName,"r")

    for line in fobj:
        print(line)

    fobj.close()

def main():

    if(len(sys.argv) == 2):
        CountWords(sys.argv[1])
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()