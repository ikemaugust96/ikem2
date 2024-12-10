import sys


def diamond_of_stars(height):
    # Calculate the number of rows for the top half
    half_height = height // 2

    # Generate the top half
    for i in range(
        half_height + (0 if height % 2 == 0 else 1)
    ):  # From 0 to half_height inclusive
        stars = "*" * (2 * i + 1)  # Calculate the number of stars
        spaces = " " * (half_height - i)  # Calculate leading spaces
        print(spaces + stars)  # Print line with leading spaces and stars

    # Generate the bottom half
    for i in range(half_height - 1, -1, -1):  # Adjust based on odd/even
        stars = "*" * (2 * i + 1)  # Calculate the number of stars
        spaces = " " * (half_height - i)  # Calculate leading spaces
        print(spaces + stars)  # Print line with leading spaces and stars


# Main execution
if __name__ == "__main__":
    # Check if height argument is provided
    if len(sys.argv) != 2:
        print("Usage: python diamond_of_stars.py <height>.Try again.")
        sys.exit(1)

    # Get the height from command line argument
    try:
        height = int(sys.argv[1])
        if height < 1:
            raise ValueError("Height must be a positive integer.Try again.")
    except ValueError:
        print("Please enter a valid integer.Try again.")

    # Call the function with the specified height
    diamond_of_stars(height)
