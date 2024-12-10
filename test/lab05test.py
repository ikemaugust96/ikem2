import sys


def optional_argument():
    if len(sys.argv) == 4 and sys.argv[3] == "striped":
        return True
    else:
        return False


def validate_arguments():
    if len(sys.argv) != 3 and (len(sys.argv) != 4 or sys.argv[3] != "striped"):
        print("usage:python3 make_a_rocket.py <width> <fuselage_length> [striped]")
        return

    try:
        width = int(sys.argv[1])
        fuselage_length = int(sys.argv[2])
        striped = optional_argument()
        return width, fuselage_length, striped

    except ValueError:
        print("Please provide a positive integer for the width and fuselage length.")
        return


def nose(width):
    if width % 2 == 0:
        for i in range(2, width, 2):
            spaces = (width - i) // 2
            print(" " * spaces + "*" * i)
    else:
        for i in range(1, width, 2):
            spaces = (width - i) // 2
            print(" " * spaces + "*" * i)


def fuselage(width, fuselage_length, striped):
    if striped:
        for i in range(fuselage_length):
            for i in range(width // 2):
                print("_" * width)
            for i in range((width + 1) // 2):
                print("x" * width)
    else:
        for i in range(fuselage_length):
            for i in range(1, width):
                print("X" * width)


def tail(width):
    for i in range(width // 2, width + 1, 2):
        spaces = (width - i) // 2
        print(" " * spaces + "*" * i)
    print("*" * width)


def main():
    width, fuselage_length, striped = validate_arguments()
    optional_argument()
    nose(width)
    fuselage(width, fuselage_length, striped)
    tail(width)


if __name__ == "__main__":
    main()
