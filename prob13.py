def add_two_numbers(n1, n2):
    
    num_len=len(n1)    
    n2='0'*(len(n1)-len(n2))+n2
    
    n1=''.join(reversed(n1))
    n2=''.join(reversed(n2))

    res=''
    carry=0

    for i in range(num_len-1):
        res+=str((int(n1[i])+int(n2[i])+carry)%10)
        carry=(int(n1[i])+int(n2[i])+carry)//10

    res=''.join(reversed(res))
    res=str(int(n1[-1])+int(n2[-1])+carry) + res

    return res

res='0'*50

with open('prob13_data.txt') as f:
    for n in f:
        res=add_two_numbers(res, n.rstrip())

print(res)
print(len(res))

#print(add_two_numbers('37107287533902102798797998220837590246510135740250',
#                      '46376937677490009712648124896970078050417018260538'))
