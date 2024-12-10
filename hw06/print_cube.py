def draw_top_back_line(n):
    # Top line with 2 * n dashes
    print(" " * (n // 2 + 1) + "+" + "-" * (2 * n) + "+")


def draw_top_sides(n):
    # Diagonal / and right vertical lines with exactly n / 2 lines for depth
    for i in range(n // 2):
        print(" " * (n // 2 - i) + "/" + " " * (2 * n) + "/" + " " * i + "|")


def draw_top_front_line(n):
    # top front line which is the same with the top bottom line
    print("+" + "-" * (2 * n) + "+" + " " * (n // 2) + "|")


def draw_front_and_right_face_top_half(n):
    # top half of the front and right face
    for i in range(n // 2 - 1):
        print("|" + " " * (2 * n) + "|" + " " * (n // 2) + "|")


def draw_central_3d_line(n):
    # central line to divide the front face into 2 halves
    print("|" + " " * (2 * n) + "|" + " " * (n // 2) + "+")


def draw_front_face_second_half(n):
    # bottom half of the front and right face
    for i in range(1, n // 2 + 1):
        print("|" + " " * (2 * n) + "|" + " " * (n // 2 - i) + "/")


def bottom_line(n):
    print("+" + "-" * (2 * n) + "+")


def print_cube(n):
    draw_top_back_line(n)
    draw_top_sides(n)
    draw_top_front_line(n)
    draw_front_and_right_face_top_half(n)
    draw_central_3d_line(n)
    draw_front_face_second_half(n)
    bottom_line(n)


def main():
    while True:
        try:
            n = int(input("Input cube size (multiple of 2): "))
            if n > 0 and n % 2 == 0:
                break
            else:
                print("Please enter a positive integer that is a multiple of 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_cube(n)


if __name__ == "__main__":
    main()
