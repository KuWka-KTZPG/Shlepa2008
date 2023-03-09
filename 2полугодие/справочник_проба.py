for N in range(516):
    b=f'{N:b}'
    if n=N % 2 ==0:
        b+= '10'
    else:
        b= '1' +b+'01'
    if int(b, 2) > 516:
        print(N)
        break
        
s = bin(i)[2:] # перевод в двоичную систему
s = str(s)
        if int(s, 2) > 441:
from turtle import *
    left(90)
    for i in range(7):
        forward(300)
        right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(5)
    done()
    while s < 51:



    from itertools import product
    nums=product('01234567', repeat=5)
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    for n in nums:
        numb=''.join(n)
        sp=[]
        if numb.count('6')==1 and numb[0]!='0':
            for x in nn:
                if x in numb:
                    sp.append(x)
            if not sp:
                k+=1
    print(k)
def f12_generator():
    sp=[]
    for num in range(2,1000):
        if all ((num%x!=0)for x in range (2,num-1)):
            sp.append(num)
    print(sp)
f12_generator()
def f14():
    alfavit=('0123456789abcde')
    for x in alfavit:
        f=int(f'123{x}5',15)+int(f'1{x}233',15)
        if f%14==0:
             print(x, f//14)
def f15():
    for A in range(1,100):
        if all (((x%2==0)<=(x%3!=0))or(x+A>=100)for x in range (1,100)):
            print(A)
            break
            
            
            
            
from itertools  import product
def f(x,y,z):
    count=0
    for i in range(1,z):
        perv=product('12',repeat=i)
        for vtor in perv:
            a=x
            if x==10 and vtor.count('2')>1:
                continue
            for o in vtor:
                if a==17:
                    break 
                if o=='1':
                    a+=1
                elif o=='2' :
                    a*=2
            if a==y: count+=1
    return count
print(f(1,10,10)*f(10,35,25))

with open('24.txt')as f:
    s=f.readline().replace('C','s').replace('D','s').replace('F','s')
    s=s.replace('A','g').replace('O','g')
    s=s.replace('sg','*')
    kmax=0
    cnt=0
    for i in range(len(s)):
        if s[i]=='*':
            cnt+=1
            kmax=max(kmax,cnt)
        else:
            cnt=0
    print(kmax)

with open('27_A.txt') as f:
    s=[x for x in f]
    s.pop(0)
    print(s)
    d=[]
    for i in s:
        d.append(i.split())
    print(d[0][1])
