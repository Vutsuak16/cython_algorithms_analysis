#finds the 1000th prime 
def prime(x):

	number=2
	primes=[]
	while len(primes) != x:

		factors=0
		for i in range(1,number+1):
			if number%i == 0:
				factors+=1

		if factors==2:
			primes.append(number)
		number+=1
		if len(primes)==x:
				print primes[-1]
				return
				



# python -m timeit --number=4 "import prime" "prime.prime(100)"