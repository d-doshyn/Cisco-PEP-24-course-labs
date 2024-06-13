input_string = input("Enter a string: ")

while True:
    try:
        input_shift_num = int(input("Enter a shift number (1-25): "))
        if input_shift_num in range(1, 26):
            break
        else:
            print("Try the number from 1 to 25")
            continue
    except:
        print("Invalid input. Try again.")
        
cipher = ''

for letter in input_string:
    letter_code = ord(letter)

    def register_checking(str1, str2):
        global letter_code
        for i in range(input_shift_num):
            letter_code += 1
            if letter_code > ord(str1):
                letter_code = ord(str2)

    if chr(letter_code).isupper():
        register_checking('Z', 'A')
    else:
        register_checking('z', 'a')

    if letter.isalpha():
        cipher += chr(letter_code)
    else:
        cipher += letter
    
print(cipher)