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
