# Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import sys
import os

def CompareFiles(File1,File2):

    Ret1 = False
    Ret1 = os.path.exists(File1)

    Ret2 = False
    Ret2 = os.path.exists(File2)

    if(Ret1 == False or Ret2 == False):
        print("File Does not exists")
        return

    fobj1 = open(File1,"r")
    fobj2 = open(File2,"r")

    Arr = fobj1.read()
    Buffer = fobj2.read()

    if(Arr == Buffer):
        print("Contents of both files are same")
    else:
        print("Contents of both files are different")

    fobj1.close()
    fobj2.close()

def main():

    if(len(sys.argv) == 3):
        CompareFiles(sys.argv[1],sys.argv[2])
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()