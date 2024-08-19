import datetime

my_date = datetime.datetime(2020, 11, 4, 14, 53)

print(my_date.strftime('%Y/%m/%d %H:%M:%S'))
print(my_date.strftime('%y/%B/%d %H:%M:%S %p'))
print(my_date.strftime('%a, %Y %b %d'))
print(my_date.strftime('%A, %Y %B %d'))
print("Weekday:", my_date.strftime('%w'))
print("Day of the year:", my_date.strftime('%j'))
print("Week number of the year:", my_date.strftime('%W'))