print("Tere tulemast!".center(50))
kool=input("\tMis koolis sa õpid?: ").capitalize() #str Kool
kursus=int(input("\tMis kuursusel?: ")) #int kursus

print("Tere tulemast kooli "+kool.upper()+"!\nOle hea "+str(kursus)+".kuursuse õpilaseks!") #kool="TTHK"

print("Tere tulemast kooli",kool.lower(),"!\nOle hea",kursus,".kuursuse õpilaseks!")#kool="tthk"

print("Tere tulemast kooli {0}!\nOle hea {1}.kuursuse õpetajaks!".format(kool,kursus))#kool="Tthk"
print(type(kool))
print(type(kursus))