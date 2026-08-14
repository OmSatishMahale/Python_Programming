# Write a program that accepts:
# • A message from the user
# • A time interval in seconds
# Schedule the program to display the message repeatedly after the specified interval.
# Example input:
# Enter message: Jay Ganesh
# Enter interval in seconds: 5
# Expected output:
# Jay Ganesh
# every five seconds.

# Validate that the interval is greater than zero.

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