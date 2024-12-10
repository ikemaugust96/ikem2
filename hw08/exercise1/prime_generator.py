# prime_generator.py


class prime_generator:
    def __init__(self, max_num):
        """Initialize with a maximum limit for prime generation."""
        self.max_num = max_num

    def primes_to_max(self, max_num):
        """Return a list of prime numbers up to max_num using the Sieve of Eratosthenes."""
        if max_num < 2:
            return []

        # Initialize a set to track non-prime numbers (composites)
        composites = set()
        primes = []

        # Sieve of Eratosthenes algorithm
        for num in range(2, max_num + 1):
            if num not in composites:
                primes.append(num)
                # Mark multiples of the prime as composite
                for multiple in range(num * 2, max_num + 1, num):
                    composites.add(multiple)

        return primes
