# Create a function named:
# DisplayMessage(message)
# Schedule the function using:
# schedule.every(5).seconds.do(DisplayMessage, message)
# The message should be accepted from the user.

import schedule
import time

def Display(message):

    print(message)

def main():

    msg = input("Enter the Message : ")
    interval = int(input("Enter the Interval : "))

    if(interval <= 0):
        print("Enter valid interval in seconds")
        print("Interval must be greater than 0 sec")
        return

    schedule.every(interval).seconds.do(Display,msg)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()