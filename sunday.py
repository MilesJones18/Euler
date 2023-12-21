'''
1 Jan 1900 was a monday.
Jan: 31
Feb: 28 LY: 29
Mar: 31
Apr: 30
May: 31
Jun: 30
Jul: 31
Aug: 31
Sep: 30
Oct: 31
Nov: 30
Dec: 31

Non-LY: 365
LY: 366

'''
from collections import OrderedDict

# OrderedDict makes sure that each element stays in the same order.
months = OrderedDict(
    [('jan',31),
    ('feb',28),
    ('mar',31),
    ('apr',30),
    ('may',31),
    ('jun',30),
    ('jul',31),
    ('aug',31),
    ('sep',30),
    ('oct',31),
    ('nov',30),
    ('dec',31)
])

days = ['tues', 'wed', 'thur', 'fri', 'sat', 'sun', 'mon']


# Iterates through each year and each month in the year, then checks if the first of that
# month is a sunday, if it is it adds it to the count, and if its a leap year, it adds an
# extra day.
def sunCalc():
    day = 0
    count = 0

    for i in range(1901, 2001):

        
        for y in months:
            dayName = days[day%7]
            if dayName == "sun":
                count += 1
            day += months[y]
            if i % 4 == 0 and y == 'feb':
                day += 1
    
    return count

print(f'Sundays: {sunCalc()}')
