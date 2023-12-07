from math import *
from random import *
#12
N=randint(2,10)
m=randint(1,10)
summa=m
print("Masinad: ",N)
print("Tunnid: ",m)
for t in range(N-1):
    m=(m/6)*7
    summa+=m
    print(m)
print("Kokku masinad töötasid:",summa,"tn")




#29
for i in range(9):
    for x in range(9):
        if x==0 or i==x:
            print("x",end=" ")
        else:
            print("0",end=" ")
    print()


print()
#15
for y in range(10):
    for x in range(10):
        print(x,end=" ")
    print()
#3
print()
p=1
lause=""
for x in range(8):
    A=float(input("{0}. samm\nSisesta A: ".format(x+1)))
    if A>0:
        p*=A
        lause=lause+str(A)+"*"

print(lause[:-1],"=",p,end="")
#1
t=0
for x in range(15):
    A=float(input("Sisesta A: "))
    if A.is_integer(): # 5.0; 6=True; 2.45=False
        t+=1
print(t)
#2
summa=0
A=int(input("Sisesta A: "))
for x in range(1,A+1,1):
    summa+=x
print("Summa: {0}".format(summa))


#for x in range(10):
#    R=float(input("{0}.R: ".format(x+1)))
#    if R>0:
#        S=pi*R**2
#    else:
#        S="R peab > kui 0 olema"
#    print("S={0}".format(S))
#x=0
#while True:
#    x+=1
#    R=float(input("{0}.R: ".format(x+1)))
#    if R>0:
#        S=pi*R**2
#    else:
#        S="R peab > kui 0 olema"
#    print("S={0}".format(S))
#    if x==10:
#        break
#10 R
#x=0
#while x<10:
#    x+=1
#    R=float(input("{0}.R: ".format(x+1)))
#    if R>0:
#        S=pi*R**2
#    else:
#        S="R peab > kui 0 olema"
#    print("S={0}".format(S))
#10 S
#x=0
#while x<10:
    
#    R=float(input("{0}.R: ".format(x+1)))
#    if R>0:
#        S=pi*R**2
#        x+=1
#    else:
#        S="R peab > kui 0 olema"
#    print("S={0}".format(S))









