#Kalkulaator
try:
    a=float(input("Esimene arv:"))
    t=input("Tehe:")
    if t in ['+','-','/','*','**','%','//']: #''=""
        pass
    else:
        print("Tundmatu märk")
    try:
        b=float(input("Teine arv:"))
        
    except :
        print("Vale andmetüüp")

except :
    print("Vale andmetüüp")






#Kolmnurk
a=float(input("Alpha:"))
b=float(input("Betta:"))
c=float(input("Gamma:"))
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
    else:
        print("Nurgad")
else:
    print("Andmed ei ole õiged")

