p=int(input("Введите основание СС: "))
Np=int(input(f"N{p}="))
k=int(1)
n10=int(0)
while not Np==0:
    n10=n10+(Np%10)*k
    k=k*p
    Np=Np//10
print("n10=", n10)
