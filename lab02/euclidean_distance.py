def main():
    # this code calculate the euclidean distance between two points
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    import math

    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("Distance between point1 and point2 is:", distance(x1, y1, x2, y2))


main()
