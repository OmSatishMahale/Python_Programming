# Schedule a task that executes every five minutes.
# The task should write the current date and time into a file named:
# Marvellous.txt
# New entries should be appended without removing previous entries.
# Example file contents:
# Task executed at: 25-07-2026 04:30:00 PM
# Task executed at: 25-07-2026 04:35:00 PM
# Task executed at: 25-07-2026 04:40:00 PM

import schedule
import time
import sys
from datetime import datetime

def Display(filename):

    now = datetime.now()
    
    fobj = open(filename,"a")
    fobj.write("Task executed at : "+now.strftime("%d-%m-%Y %I:%M:%S %p"+"\n"))

    fobj.close()

def main():

    if(len(sys.argv) == 2):
        schedule.every(1).seconds.do(Display,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()