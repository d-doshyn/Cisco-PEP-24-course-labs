input_date = input("Enter your date of birth (ddmmyyyy): ")

date_sum = int(input_date)

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

while date_sum > 10:
    date_sum = sum_of_digits(date_sum)

print(date_sum)