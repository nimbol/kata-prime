import pytest

import prime


@pytest.mark.parametrize("n", (0, 1, 4, 6))
def test_is_prime_false(n):
    assert False


@pytest.mark.parametrize("n", (2, 3, 5, 7))
def test_is_prime_true(n):
    assert False


def test_prime_generator():
    primes = prime.prime_generator()
    assert False


def test_prime_sieve():
    primes = prime.prime_sieve(100)
    assert False
