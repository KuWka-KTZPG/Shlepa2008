from itertools import product
tab=[[0,712,673,1075,875,1622,423],
     [712,0,1385,1800,1577,2348,1128],
     [673,1385,0,1499,239,2046,244],
     [1075,1800,1499,0,1287,551,1266],
     [875,1577,239,1287,0,1835,442],
     [1622,2348,2046,551,1835,0,1813],
     [423,1128,244,1266,442,1813,0]]
st='0123456'
s=product(st, repeat=7)
summ=0
g=0
for i in s:
    if all(i.count(s)==1 for s in st):
        for k in range(len(i)-1):
            summ+=tab[int(i[k])][int(i[k+1])]
        if summ>g:
            g=summ
        summ=0
print(g)
