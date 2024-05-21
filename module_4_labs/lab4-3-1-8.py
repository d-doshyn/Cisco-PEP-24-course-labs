def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    
    if is_year_leap(year) == True and month == 2:
        return 29
        
    if is_year_leap(year) == False:
        if month == 2:
            return 28
        
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    leap_year_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    common_year_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year):
        return sum(leap_year_days[:month-1]) + day
    else:
        return sum(common_year_days[:month-1]) + day

print(day_of_year(2034, 12, 31))