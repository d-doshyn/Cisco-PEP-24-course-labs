def readint(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if (value >= min) and (value <= max):
                return value
            else:
                print("Error: not within permitted range")
                continue
        except:
            print("Error: wrong input")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)