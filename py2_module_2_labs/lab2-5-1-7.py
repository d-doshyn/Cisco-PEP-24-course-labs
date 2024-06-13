while True:
    input_value = input("Enter some value: ")
    if input_value.isspace():
        print("The string should not be empty! Try again!")
        continue
    else:
        break

val_to_work = input_value.lower().replace(' ', '')

if val_to_work == val_to_work[::-1]:
    print("It is a palindrome!")
else:
    print("Not a palindrome")