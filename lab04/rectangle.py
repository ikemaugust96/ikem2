def rectangle(symbol, width, height):
    # rule out input of width ot height <2
    if width < 2:
        print("The width must be at least 2.")
    if height < 2:
        print("The height must be at least 2.")
        return

    # first line
    print(symbol * width)
    # second line to the last but one line
    for _row in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)
    # last line
    print(symbol * width)


# get input and run the module
def main():
    symbol = input("Enter a symbol for the rectangle: ")
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    rectangle(symbol, width, height)


main()
