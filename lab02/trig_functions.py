def main():
    # this code calculate the sine and cosine value of the angle
    x = float(input("x: "))
    import math

    def sin(x):
        return math.sin(math.radians(x))

    def cos(x):
        return math.cos(math.radians(x))

    print("sin of x is", sin(x), "and cos of x is", cos(x))


main()
