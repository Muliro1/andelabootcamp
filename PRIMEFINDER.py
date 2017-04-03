 def primeFinder(n):
	primes = []
	for i in range(n + 1):
		isPrime = True
		for x in range(2, i):
			if i % x == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(i)
	return primes
