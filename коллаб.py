def f1_1():
#ИЗ 10 В ДРУГУЮ
N10=int(input(f"Введите число в десятичной системе счисления >>> "))
NN=N10
Np=int(0)
k=int(1)
p=int(input(f"Введите основание системы счисления, в которую нужно перевести число >>> "))
while N10!=0:
    Np=Np+(N10%p)*k
    k=k*10
    N10=N10//p
print(f"Число {NN} в {p}-ичной системе счисления равно {Np}")
def f1_2():
#ПЕРЕВОД ИЗ НЕДЕСЯТИЧНОЙ СИСТЕМЫ СЧИСЛЕНИЯ
p=int(input("Введите основание СС: "))
Np=int(input(f"число в СС по основанию {p}="))
k=int(1)
n10=int(0)
while not Np==0:
    n10=n10+(Np%10)*k
    k=k*p
    Np=Np//10
print("n10=", n10)
def f1_3():
#ИЗ 10 В ДРУГУЮ
x=int(1)
y=int(1)
z=int()
p=int(input("Введите основание степени счисления >>> "))
print(f"{p}- ичная система счисления")
for x in range (1,p):
    for y in range (1,p):
        z=(x*y//p)*10+(x*y)%p
        print(z,end=' ')
    print()
def f2():
#МОРЗЯНКА
a = "abwgdevijklmnoprstufhcqx"
abc = list(a)
print(abc)
b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
abcm=b.split()
print(abcm)
abcm=b.split()
text=input("Введите текст на английском: ")
indm=""
for i in range (len(text)):
    ind = abc.index(text[i])
    indm=indm + abcm[ind] 
print(f"{indm}строка  в азбуке морзе")
def f3():
#ХЕММИНГ
a='0123456789'
nums=list(a)
print(nums) 
b='0000000 0001111 0010110 0011001 000101 0101010 0110011 0111100 1000011 1001100'
hem=b.split()
print(hem)
for i in range(len(hem)):
  hem[i]=int(hem[i])
print(hem))
def distance(x,y):
  k=7
  for i in range(7):
    if x%10==y%10:
      k=k-1
    x=x//10
    y=y//10
  return k
cod=int(input("код"))
min=distance(cod,hem[0])
imin=0
for i in range(10):
  D=distance(cod,hem[i])
  if D

if min==0:
    print(f"код верный: символ {nums[imin]}")
elif min==1:
    print(f"код исправлен: символ {nums[imin]}")
else:print("Код неверный")




#ИЗ 10 В ДРУГУЮ
N10=int(input(f"Введите число в десятичной системе счисления >>> "))
Np=int(0)
k=int(1)
p=int(input(f"Введите основание системы счисления, в которую нужно перевести число >>> "))
while N10!=0:
    Np=Np+(N10%p)*k
    k=k*10
    N10=N10//p
print(f"Число {N10} в {p}-ичной системе счисления равно {Np}")







