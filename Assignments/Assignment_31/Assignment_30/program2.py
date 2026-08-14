# Write a Python program that displays the current date and time
# after every one minute.
# Use the datetime module.
# Expected output:
# Current Date and Time: 25-07-2026 04:30:00 PM

import schedule
from datetime import datetime
import time

def DisplayDateTime():

    now = datetime.now()

    print("Current Date and Time : ",now.strftime("%d-%m-%Y %I:%M:%S"))

def main():

    schedule.every(1).minute.do(DisplayDateTime)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()