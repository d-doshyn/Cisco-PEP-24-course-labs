blocks = int(input("Enter the number of blocks: "))
height = 0
iter_counter = 1

while blocks >= 0:
    if blocks < iter_counter:
        break
    
    blocks -= iter_counter
    iter_counter += 1
    height += 1

print("The height of the pyramid:", height)