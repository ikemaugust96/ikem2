import sys


def fibonacci_sequence(n):
    if n == 1:
        return [0]  # Special case for N=1
    elif n == 2:
        return [0, 1]  # Special case for N=2

    # Start with the first two Fibonacci numbers for N > 2
    sequence = [0, 1]

    # Generate the remaining Fibonacci numbers
    for i in range(2, n):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)

    return sequence


def main():
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <number>. Try again.")
        return

    # Check if the argument is a digit
    if sys.argv[1].isdigit():
        number = int(sys.argv[1])

        # Make sure the number is greater than 0
        if number > 0:
            # Generate and print the Fibonacci sequence
            sequence = fibonacci_sequence(number)
            print(sequence)
        else:
            print("Please enter a positive integer in command line.\
                  Try again. ")
    else:
        print("Please enter a valid integerin command line.Try again.")
        return


if __name__ == "__main__":
    main()
