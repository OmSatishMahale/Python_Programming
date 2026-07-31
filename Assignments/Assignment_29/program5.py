# Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.
# Om Om Om

import sys
import os

def WordFrequency(FileName,Word):

    Ret = False
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("File Does not exists")
        return

    fobj = open(FileName,"r")
    freq = 0

    for line in fobj:
        word = line.split()
        if Word in word:
            freq = freq + word.count(Word)

    fobj.close()

    print(f"Frequency of '{Word}' in '{FileName}' is: {freq}")

def main():

    if(len(sys.argv) == 3):
        WordFrequency(sys.argv[1],sys.argv[2])
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()