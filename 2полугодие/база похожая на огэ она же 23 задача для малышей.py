from itertools  import product
def f():
    count = 0
    for i in range (2,10):
        b=product('12', repeat=i)
        for n in b:
            a=1
            for x in n:
                if x =="1":a+=1
                else:a*=2
            if a==10:
                count+=1
    print(count)
#print(n)

def g():
    count10 = 0
    for i in range (2,24):
        b=product('12', repeat=i)
        for n in b:
            a10=10
            for x in n:
                if x =="1":a10+=1
                else:a10*=2
            if a10==17: break
            if a10==35:
                count10+=1
    print(count10)
f()
g()
