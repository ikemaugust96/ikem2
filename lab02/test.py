def base_width(width):
    # rule out input of width ot height <2
    if width <= 2 or width % 2 != 0:
        print("The width must be an odd number greater than 3.")
    return
    tree_height = ((width) + 1) // 2
    # Print the top of the tree
    print(" " * (tree_height - 1) + "*")
    # Print the tree's body
    for i in range(1, tree_height):
        spaces = " " * (tree_height - i - 1)
        middle = " " * (2 * i - 1)
    print(spaces + "/" + middle + "\\")
    print("/" + "_" * (width - 2) + "\\")


def main():
    width = int(input("please enter the base width:"))


base_width()
main()
