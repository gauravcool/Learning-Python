#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=1))

# print today's date
now = datetime.now()
print("Now date is: "+str(now))

# print today's date one year from now
print("Date one year from now: "+str(now+timedelta(days=365)))

# create a timedelta that uses more than one argument
print("Time from 3 days 4 weeks from now: "+str(now+timedelta(days=3,weeks=4)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %d, %Y")
print("One week ago: "+s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fool's day already went by %d days ago"%((today-afd).days))
    afd = afd.replace(year = today.year+1)

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print("It's just", time_to_afd.days, "days until April fool's day")

