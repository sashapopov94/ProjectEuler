a=list(range(2, 10**4+1))
while min(a)!=101:
    min_=min(a)
    a.remove(min_)
    a.append(min_**2)

a=sorted(a)
print(len(a))

res=[]
for i in range(9890):
    tmp=a[i]
    l=[]
    for j in range(28):
        tmp=(tmp*tmp)%(1234567891)
        l.append(tmp)
    tmp=1
    for j in range(606):
        tmp=(tmp*a[i])%(1234567891)
    
    res.append((l[27]*l[26]*l[25]*l[24]*l[22]*l[19]*l[16]*l[15]*l[13]*l[12]*l[10]*tmp)%(1234567891))

for x in a[9890:]:
    tmp=x
    l=[]
    for j in range(29):
        tmp=(tmp*tmp)%(1234567891)
        l.append(tmp)
    tmp=1
    for j in range(664):
        tmp=(tmp*x)%(1234567891)
    
    res.append((l[28]*l[27]*l[25]*l[19]*l[17]*l[14]*l[12]*l[11]*l[9]*tmp)%(1234567891))

print(res)
print(len(res))
print(sum(res)%(1234567891))

