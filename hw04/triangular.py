import sys


def triangular_number(n):
    # The triangular number is the sum of all integers from 1 to n.
    return n * (n + 1) // 2


def main():
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 2:
        print("Usage: python triangular.py <number>")
        return

    # Check if the argument is a digit
    if sys.argv[1].isdigit():
        number = int(sys.argv[1])

        # Ensure the number is positive
        if number > 0:
            result = triangular_number(number)
            print(f"The triangular number of {number} is :{result}.")
        else:
            print("Please enter a positive integer in command line.Try again.")
    else:
        print("Please enter a valid integer in command line.Try again")
        return


if __name__ == "__main__":
    main()
