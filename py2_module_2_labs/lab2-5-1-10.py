main_string = input("Enter main string: ")
str_contains_main = input("Enter string that can contain main: ")

iter_letters = []
str_to_work = str_contains_main[:]

for char in main_string:
    str_to_work = str_to_work[str_to_work.find(char):]
    iter_letters.append(str_to_work[0])

compare_str = ''.join(iter_letters)

if main_string == compare_str:
    print("Yes")
else:
    print("No")