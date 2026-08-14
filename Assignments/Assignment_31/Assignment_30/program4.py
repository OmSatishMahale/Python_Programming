# Write a program that schedules a function to print:
# Coding Kar..!
# every 30 minutes.

import schedule
import time

def Display():

    print("Namaskar")

def main():

    schedule.every().day.at("20:00").do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()