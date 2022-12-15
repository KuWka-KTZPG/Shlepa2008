#мальчик 1
def f(familie):
    print(familie[::-1])
#мальчик 2
def g(pol, familie):
    mal_2=pol +" "+ (familie[::-1])
    return mal_2


def u(familie):
    fam_glas=list('уеаоэёяию')
    for i in familie:
        if i in fam_glas:
            print(i)
        




    
#прога
familie=input("Напшите фамилию: ")
f(familie)
print("////////")
pol=input("ведите пол мальчика: ")
print(g(pol , familie))
print("Гласные: ")
u(familie)




