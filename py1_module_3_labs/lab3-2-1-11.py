word_without_vowels = ""

user_word = input("Enter the word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "O" or letter == "U" or letter == "I":
        continue
    else:
        word_without_vowels += letter
        
print(word_without_vowels)