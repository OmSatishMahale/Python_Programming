#Continue from Automation FOlder

import sys                  
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Path is invalid")
        return

    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("It is not a Directory")
        return

    Duplicate = {}
    Unique = 0
    Same = 0

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            print(f"{fname} : {CheckSum}")

            Unique = Unique + 1
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate
def main():
    Data = FindDuplicate("Test")
    print("Duplicate Files are : ",Data)
    
if __name__ =="__main__":
    main()