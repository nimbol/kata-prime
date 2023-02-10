import itertools

import pytest

import prime


# @pytest.mark.parametrize("n", (0, 1, 4, 6))
# def test_is_prime_false(n):
#     assert False


# @pytest.mark.parametrize("n", (2, 3, 5, 7))
# def test_is_prime_true(n):
#     assert False


def test_prime_generator():
    primes = prime.prime_generator()

    assert next(primes) == 2
    assert next(primes) == 3
    assert next(primes) == 5
    assert next(primes) == 7


def test_prime_generator__first_ten():
    primes = prime.prime_generator()

    assert list(itertools.islice(primes, 0, 10)) == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
    ]


def test_prime_sieve():
    primes = prime.prime_sieve(30)
    assert primes == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
    ]
