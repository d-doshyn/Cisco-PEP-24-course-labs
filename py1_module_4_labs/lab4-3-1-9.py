def is_prime(num):
    if num <= 1:
        return False
        
    for i in range(2, num):
        check = num % i == 0
        if check == True:
            return False
            
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()