import datetime as dt

class Primes:
    
    def __init__(self, n, sieve):
        self.n = n
        self.sieve = sieve

    def __getitem__(self, n):
        next_prime = next(self.sieve)
        self.sieve = filter(lambda x: x%next_prime, self.sieve)
        return next_prime


def numbers(limit):
    num = 2
    while num <= limit:
        yield num
        num += 1

def infinite_numbers():
    num = 2
    while True:
        yield num
        num += 1

#ints = numbers(775146)
ints = infinite_numbers()

primes = Primes(1, ints)
it = iter(primes)

# Save the current time to a variable ('t')
#t = dt.datetime.now()

#for i in range(775146):
#    delta = dt.datetime.now()-t
#    d = next(it)
#    if delta.seconds >= 60:
#        print("time d", d)
#        # Update 't' variable to new time
#        t = dt.datetime.now()
#    if 600851475143%d == 0:
#        print(d)


# Problem 7

#for i in range(10000):
#    next(it)

#print("10 001-st prime is {0}".format(next(it)))

# Problem 10

p = next(it)
sum_of_primes = 0

while p < 2000000:
	print("p = ", p)
	sum_of_primes += p
	p = next(it)

print("Sum of primes under 2 million = {0}".format(sum_of_primes))



