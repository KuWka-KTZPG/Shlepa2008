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
