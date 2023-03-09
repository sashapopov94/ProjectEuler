def prob14():
    max_count=1
    for i in range(2, 10**6):
        print("i=", i, "\n")
        n=i
        curr_count=0    
        while n!=1:
            curr_count+=1
            if n%2: # odd number
                n=3*n+1
            else:
                n=n/2
        if max_count < curr_count:
            res=i
            max_count=curr_count
    return res


print(prob14())

