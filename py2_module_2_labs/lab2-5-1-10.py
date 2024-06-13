main_string = input("Enter main string: ")
str_contains_main = input("Enter string that can contain main: ")

letters_index_list = []

for i in main_string:
    letters_index_list.append(str_contains_main.find(i))

if -1 in letters_index_list:
    print("No")
else:
    print("Yes")