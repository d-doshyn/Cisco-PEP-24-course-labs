some_int = int(input("Enter some integer: "))
int_to_str = str(some_int)

main_str = ""
        
patterns = [
    ["### ", "# # ", "# # ", "# # ", "### "],
    ["  # ", "  # ", "  # ", "  # ", "  # "],
    ["### ", "  # ", "### ", "#   ", "### "],
    ["### ", "  # ", "### ", "  # ", "### "],
    ["# # ", "# # ", "### ", "  # ", "  # "],
    ["### ", "#   ", "### ", "  # ", "### "],
    ["### ", "#   ", "### ", "# # ", "### "],
    ["### ", "  # ", "  # ", "  # ", "  # "],
    ["### ", "# # ", "### ", "# # ", "### "],
    ["### ", "# # ", "### ", "  # ", "### "]
]

for j in range(5):
    for integer in int_to_str:
        main_str += patterns[int(integer)][j]
    main_str += '\n'
    
print(main_str)