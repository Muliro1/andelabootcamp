import unittest
from PRIMEFINDER import prime_finder

class testCase(unittest.Testcase):
        def test_returns_primes_only(self):
                self.assertEqual(prime_finder(10), [2,3,5,7])
        def test_returns_integerlist(self):
                self.assertEqual(prime_finder(20), [2,3,5,7,11,13,17,19])
        def test_if_negative_or_zero_argument(self):
                self.assertEqual(prime_finder(0), 'Invalid Argument')
        def test_if_arg_is_not_integer(self):
                self.assertEqual(prime_finder('string'), 'Invalid Argument')
        def test_if_empty(self):
                self.assertEqual(prime_finder(), 'Function requires an integer argument')

def prime_finder(n):
        # this function takes in an integer n and returns a list of prime numbers from 0 to n
        if bool(n) == False:
                return 'Function requires an integer argument'
        if n <= 0 or not isinstance(n, int):
                return 'Invalid Argument'
        else:
                primes = []
                for i in range(n + 1):
                        if i == 0 or i == 1:
                                isPrime = False
                        else:
                                isPrime = True
                                for x in range(2, i):
                                        if i % x == 0:
                                                isPrime = False
                                                break
                        if isPrime:
                                primes.append(i)
        return primes

