from random import *
#7
kokku=randint(1,20)
num_list=[]
for i in range(kokku):
    num_list.append(randint(-100,100))
print("\tOriginaal:")
print(num_list)
for element in num_list:
    if element<0:
        n=num_list.index(element)
        num_list[n]=abs(element)

print("\tAbsoluut värtused:")
print(num_list)
num_list.sort()
print("\tKasvav järjend:")
print(num_list)
num_list.reverse()
print("\tKahanev järjend:")
print(num_list)



for i in range(5):
    print()
#6
kokku=randint(2,20)
print("kokku järjedis on: ",kokku,"elementi")
num_list=[]
for i in range(kokku):
    num_list.append(round(random()*1000,2))
print(num_list)
max_=max(num_list)
n=num_list.index(max_)
print("\t",max_,"positsioonil:",n+1)
num_list.pop(n)
max_=max_/len(num_list)
num_list.insert(n,max_)
print(num_list)


for i in range(5):
    print()
#5

kokku=randint(2,20)
num_list=[]
for i in range(kokku):
    num_list.append(randint(-100,100))
print(num_list)
print()
while True:
    try:
        kogus=int(input("Mitu positsiooni vahetada?"))
        if kogus<=kokku/2:
            break
    except :
        print("Proovi uuesti")







#4 Index
indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa"," Läänemaa, Hiiumaa, Saaremaa"]
while True:
    try:
        index=int(input("Sisesta postindex"))#12345
        if len(str(index))==5: #"12345"
            break
    except :
        print("Viga!")
print("Indexi analüüs")
index_list=list(str(index))
s1=int(index_list[0]) #1->0 Tallin indexiga 0
print("Index {0} on {1} piirkonnas".format(index,indexid[s1-1]))



#2
l=[11,1,1,1,1,1,1,2,3,4,1,2,33]
l_set=set(l)
print(l_set)
for e in l_set:
    print(e*"*")




import string
#1
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti="qwrtpsdfghklzxcvbnm"
markid=string.punctuation
v=k=m=t=0 #vokaali #konsonanti# kirjuvahemärgid# tühikud
while True:
    tekst=input("Sisesta sõna või lause: ")#.lower()
    if tekst.isdigit(): 
        break
    else:
        tekst_l=list(tekst)
        print(tekst_l)
        for e in tekst_l:
            if e.lower() in vokaali: 
                v+=1
            elif e.lower() in konsonanti:
                k+=1
            elif e.lower() in markid:
                m+=1
            elif e.lower()==" ":
                t+=1
    print("Vokaali:",v)
    print("Konsonanti:",k)
    print("Kirjuvahemärgid:",m)
    print("Tühikud:",t)
