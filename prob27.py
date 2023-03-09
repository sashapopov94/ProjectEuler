res=[]
for p in primes:
    l=int(math.sqrt(4*p))
    for a in range(-l, l+1, 1):
        inc=1
        counter=0
        next_prime=p+a+inc
        while next_prime in all_primes:
            counter+=1
            inc+=2
            next_prime+=a+inc
        res.append((counter, a, p))
