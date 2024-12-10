from prime_generator import prime_generator


def main():
    while True:
        try:
            max_num = int(
                input("Enter the maximum number up to which to find primes: ")
            )
            if max_num < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    prime_gen = prime_generator()
    primes = prime_gen.primes_to_max(max_num)
    print(f"Primes up to {max_num}:")
    print(primes)


if __name__ == "__main__":
    main()
