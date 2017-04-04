def prime_finder(n):
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

