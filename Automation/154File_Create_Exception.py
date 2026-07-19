def main():

    try:
        open("Demo.txt","w")        #It is used to write as well as create the file
        print("File gets Opened")

    except FileNotFoundError as fobj:
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()