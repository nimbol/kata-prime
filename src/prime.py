"""
Calculate the 1,000,000th prime number.
This is an exercise in optimisation, iteration and problem solving.
Possible approaches are outlined below.
"""
from typing import List, Optional, Sequence


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


def prime_sieve(limit: int) -> List[int]:
    """
    Calculate the full sequence of primes up to a certain limit by
    using the sieve of Eratosthenes algorithm.
    This approach is pretty efficient, but obviously literally limited.
    """
