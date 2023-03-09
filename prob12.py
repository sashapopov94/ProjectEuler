class Primes:
    
    def __init__(self, n, sieve):
        self.n = n
        self.sieve = sieve

    def __getitem__(self, n):
        next_prime = next(self.sieve)
        self.sieve = filter(lambda x: x%next_prime, self.sieve)
        return next_prime


def infinite_numbers():
    num = 2
    while True:
        yield num
        num += 1

ints = infinite_numbers()
primes = Primes(1, ints)
it = iter(primes)
a = [0]*2000

for i in range(2000):
    p = next(it)
    a[i] = p

def count_divisors(n):
    
    if n==1:
        return 1

    i=0
    ans=1
    while(1):
        
        if a[i] > n:
            break

        cnt=1
        while(n % a[i] == 0):
            n /= a[i]
            cnt += 1

        ans *= cnt
        i+=1

    return ans

tr_number = 1

for i in range(2,50000):
    tr_number += i    
    if count_divisors(tr_number) > 500:
        print(tr_number)

    
    
