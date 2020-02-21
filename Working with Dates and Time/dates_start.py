#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is: ",today)



  # print out the date's individual components
  print("Individual comp: ",today.day,today.month,today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Weekday: ",today.weekday())
  days = ['mon','tue','wed','thu','fri','sat','sun']
  print("Weekday: ",days[today.weekday()])

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  date1 = datetime.now()
  print(date1)

  # Get the current time
  print(date1.time())

  
if __name__ == "__main__":
  main();
  