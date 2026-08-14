# Write a program that creates a new log file after every ten minutes.
# The filename should contain the current date and time.
# Example:
# MarvellousLog_25_07_2026_16_30_00.txt
# The file should contain:
# Log file created successfully.
# Creation Time: 25-07-2026 04:30:00 PM  ("%d-%m-%Y %H:%M:%S %p")

import time
import os
from datetime import datetime
import schedule

def CreateLogFile():

    time = datetime.now()

    LogFileName = "MarvellousLog_" + time.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(LogFileName,"w")
    fobj.write("Log File gets Successfully Created at : "+time.strftime("%d-%m-%y %H:%M:%S %p"))

    fobj.close()


def main():

        schedule.every(10).seconds.do(CreateLogFile)

        while(True):
             schedule.run_pending()
             time.sleep(1)

if __name__ == "__main__":
    main()