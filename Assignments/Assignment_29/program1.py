# Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import sys
import os

def CheckFileExists(FileName):
    if os.path.exists(FileName):
        print(f"File '{FileName}' exists.")
    else:
        print(f"File '{FileName}' does not exist.")

def main():
    if len(sys.argv) == 2:
        CheckFileExists(sys.argv[1])
    else:
        print("Invalid number of arguments.")

if __name__ == "__main__":
    main()