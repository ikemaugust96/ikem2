def is_magic_square(square):
    # Check that all rows, columns, and diagonals sum to 15
    target_sum = 15

    # Extract rows
    row1 = square[0]
    row2 = square[1]
    row3 = square[2]

    # Calculate the sums for rows, columns, and diagonals
    rows = [sum(row1), sum(row2), sum(row3)]
    cols = [
        sum([row1[0], row2[0], row3[0]]),
        sum([row1[1], row2[1], row3[1]]),
        sum([row1[2], row2[2], row3[2]]),
    ]
    diagonals = [row1[0] + row2[1] + row3[2], row1[2] + row2[1] + row3[0]]

    # Check if all sums are 15
    return all(s == target_sum for s in rows + cols + diagonals)


# check if the square uses each 1-9 one time
def has_valid_numbers(square):
    flat_list = [num for row in square for num in row]
    return sorted(flat_list) == list(range(1, 10))


def main():
    # Collect input for 3 rows
    square = []
    print("Enter a magic square:")
    for _ in range(3):
        row = list(map(int, input().strip()))
        square.append(row)

    # Validate the square
    if is_magic_square(square) and has_valid_numbers(square):
        print("This is a magic square!")
    else:
        print("Not a magic square!")


main()
