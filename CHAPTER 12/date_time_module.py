import datetime

x = datetime.datetime.now() # gives system's current time and date.
print("Current date and time is:",x)
print("------------------------------")
year_full = x.strftime("%Y") # retrive year only from x variable contains system's current date and time.
print('Current year only:',year_full)

print("------------------------------")

year_half = x.strftime("%y")
print('Current year:',year_half)

print("------------------------------")

Hour_12 = x.strftime("%I")
print('Current hour in 12 :',Hour_12)

print("------------------------------")

month_full = x.strftime("%B")
print('Current month:',month_full)

print("------------------------------")

Hour_24 = x.strftime("%H")
print('Current hour in 24:',Hour_24)

print("------------------------------")

am_pm = x.strftime("%p")
print('Current time slot:',am_pm)

print("------------------------------")


