# Get valid odd number input
while True:
    base_width = int(
        input("Enter an odd number (3 or greater) for the base width of the tree: ")
    )
    if base_width >= 3 and base_width % 2 != 0:
        break
    else:
        print("Invalid input. Please enter an odd number greater than or equal to 3.")

# Calculate the number of levels (tree height)
tree_height = (base_width + 1) // 2

# Print the top of the tree
print(" " * (tree_height - 1) + "*")

# Print the tree's body
for i in range(1, tree_height):
    spaces = " " * (tree_height - i - 1)
    middle = " " * (2 * i - 1)
    print(spaces + "/" + middle + "\\")

# Print the base
print("/" + "_" * (base_width - 2) + "\\")
