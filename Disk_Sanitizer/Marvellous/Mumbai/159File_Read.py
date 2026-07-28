def main():

    try:
        fobj = open("Demo.txt","r") 
        print("File gets Opened")

        Data = fobj.read(10)          #It reads the data from file(Demo.txt) and store it in Data Array

        print(Data)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()