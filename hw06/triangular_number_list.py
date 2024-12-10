def triangular_number(n):
    """
    Calculate the nth triangular number.
    A triangular number is given by the formula n * (n + 1) / 2.
    """
    return n * (n + 1) // 2


def main():
    # Initialize an empty list to store triangular numbers
    triangular_numbers = []

    while True:
        # Prompt the user for input
        user_input = input("Enter a number, or enter 'done': ")

        if user_input.lower() == "done":
            break  # Exit the loop when the user types 'done'

        # Convert input to an integer
        num = int(user_input)

        # Calculate the triangular number
        tri_num = triangular_number(num)
        print(f"The triangular number for {num} is {tri_num}")

        # Append the triangular number to the list
        triangular_numbers.append(tri_num)

    # Print the final list of triangular numbers
    print(triangular_numbers)


# Run the main function if this script is executed
if __name__ == "__main__":
    main()
