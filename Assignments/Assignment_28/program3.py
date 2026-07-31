# Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the
# screen.
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo.txt one by one.

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