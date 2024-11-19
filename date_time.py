import time
ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

print("localtime:", time.localtime())

localtime = time.localtime(time.time())
print("local current time:", localtime)


import calendar
cal = calendar.month(2024,4)
print("Here is the calendar:")
print(cal)


print()

from  datetime import date
date1 = date(2024,11,14)
print("date:", date1)
date2 = date(2024,11,20)

