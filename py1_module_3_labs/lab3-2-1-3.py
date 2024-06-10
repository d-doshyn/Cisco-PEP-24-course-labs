secret_number = 777
guess_number = int(input("try to guess the number: "))

while guess_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess_number = int(input("try to guess the number: "))
        
print("Well done, muggle! You are free now. The number is", guess_number)