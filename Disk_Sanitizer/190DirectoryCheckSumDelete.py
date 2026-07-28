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


    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            print(f"{fname} : {CheckSum}")

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate

def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)

    Result = list(filter((lambda x : len(x) > 1),MyDict.values()))

    return Result

def main():
    Data = FindDuplicate("Test")
    print("Duplicate Files are : ",Data)
    
if __name__ =="__main__":
    main()