import sys


def main(max_val):
    """
    Print out prime numbers
    from 2 to max_val
    """

    START_VAL
    START_DIVISOR = 2

    print(START_VAL)

    candidate = START_VAL + 1

    while candidate <= max_val:
        is_prime = True

        div = START_DIVISOR

        while div < candidate:
            if not (candidate % div):
                is_prime = False
            div += 1

        if is_prime:
            print(candidate)

        candidate += 1


main(int(sys.argv[1]))
