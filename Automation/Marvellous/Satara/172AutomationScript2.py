import sys                  #for getting command lines arguments

def main():

    if(len(sys.argv) == 2):
        DirectoryName = sys.argv[1]
        print("DIrectory name is : ",DirectoryName)
    else:
        print("Invalid Numbers of Arguments")

if __name__ =="__main__":
    main()