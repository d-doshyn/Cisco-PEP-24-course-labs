hat_list = [1, 2, 3, 4, 5]  

hat_list[2] = int(input("Enter second element:"))
print("Step 1:", hat_list)

del hat_list[-1]
print("Step 2:", hat_list)

print("Step 3:", len(hat_list))