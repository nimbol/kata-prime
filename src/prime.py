"""
Calculate the 1,000,000th prime number.
This is an exercise in optimisation, iteration and problem solving.
Possible approaches are outlined below.
"""
from typing import List, Optional, Sequence
import math


def is_prime(n: int, known_primes: Sequence[int]) -> bool:
    """
    This approach seems inefficient if used to test each individual number.
    May work well for individual large numbers.
    """


def prime_generator() -> Sequence[int]:
    """
    Just start from the beginning and keep yielding calculated primes.
    This approach is simple and may become inefficient for large numbers.
    """
    yield 2
    num = 1
    divisor = 3
    while True:
        num += 2
        divisor = 3
        while divisor <= math.isqrt(num):
            if num % divisor == 0:
                break
            divisor += 2
        else:
            yield num


def prime_sieve(limit: int) -> List[int]:
    """
    Calculate the full sequence of primes up to a certain limit by
    using the sieve of Eratosthenes algorithm.
    This approach is pretty efficient, but obviously literally limited.
    """
    possibilities = list(range(3, limit + 1, 2))
    idx = 0
    max_test = math.sqrt(limit + 1)
    while possibilities[idx] < max_test:
        p = possibilities[idx]
        for n in range(p * p, limit + 1, p * 2):
            try:
                possibilities.remove(n)
            except ValueError:
                pass
        idx += 1
    return [2] + possibilities


if __name__ == "__main__":
    print(prime_sieve(100_000)[-1])
    # g = prime_generator()
    # for _ in range(100_000):
    #     next(g)
    # for _ in range(900_000):
    #     print(next(g))
