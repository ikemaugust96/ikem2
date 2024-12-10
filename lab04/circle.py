import sys
import math


def print_circle(radius):
    # Loop through a 2D grid that fits the circle
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            # Adjusting the condition to make a wider, rounder circle
            if math.sqrt((x * 2) ** 2 + y**2) <= radius:
                print("O", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line


def main():
    if len(sys.argv) != 2:
        print("Usage: python circle.py <radius>")
        return

    # Get the radius from the command line
    try:
        radius = int(sys.argv[1])
        if radius < 1:
            raise ValueError
    except ValueError:
        print("Please provide a positive integer for the radius.")
        return

    # Print the circle with the given radius
    print_circle(radius)


main()
