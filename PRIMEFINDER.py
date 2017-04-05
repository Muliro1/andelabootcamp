

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

