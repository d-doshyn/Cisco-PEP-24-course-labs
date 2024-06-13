first_val = input("Enter the first value: ").lower().replace(' ', '')
second_val = input("Enter the second value: ").lower().replace(' ', '')

if sorted(list(first_val)) == sorted(list(second_val)):
    print("Anagram")
else:
    print("Not an anagram")