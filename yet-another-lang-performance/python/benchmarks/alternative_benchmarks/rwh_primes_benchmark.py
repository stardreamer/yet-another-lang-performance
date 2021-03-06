from benchmarks.benchmark import Benchmark


class RwhPrimesBenchmark(Benchmark):
    primes_number = 10

    @staticmethod
    def __primes(n):
        """ Returns  a list of primes < n """
        """ https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188"""
        sieve = [True] * n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * int(((n - i * i - 1) / (2 * i) + 1))
        return [2] + [i for i in range(3, n, 2) if sieve[i]]

    def __init__(self, primes_number: int):
        self.primes_number = primes_number
        super().__init__("RWH primes basic")

    def get_hidden_result(self):
        return self.__primes(self.primes_number)

    def _execute_impl(self):
        self.__primes(self.primes_number)
