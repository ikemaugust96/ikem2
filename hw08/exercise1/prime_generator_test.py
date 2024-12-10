# prime_generator_test.py

from prime_generator import prime_generator


def test_primes_to_max():
    prime_gen = prime_generator()

    # Known primes for testing
    assert prime_gen.primes_to_max(10) == [2, 3, 5, 7]
    assert prime_gen.primes_to_max(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert prime_gen.primes_to_max(1) == []
    assert prime_gen.primes_to_max(2) == [2]
    assert prime_gen.primes_to_max(0) == []

    # Additional test cases
    primes_up_to_30 = prime_gen.primes_to_max(30)
    assert 29 in primes_up_to_30  # Verify a prime near the upper limit
    assert 28 not in primes_up_to_30  # Verify a non-prime is excluded


if __name__ == "__main__":
    try:
        test_primes_to_max()
        print("All tests passed")
    except AssertionError:
        print("Some tests failed")
