print("Tere tulemast!")
kool=input("Mis koolis sa õpid?: ") #str kool
kursus=int(input("Mis kuursusel?: ")) #int kursus
print("Tere tulemast kooli "+kool+"!\nOle hea "+str(kursus)+".kuursuse õpilaseks!")
print("Tere tulemast kooli",kool,"!\nOle hea",kursus,".kuursuse õpilaseks!")
print("Tere tulemast kooli {0}!\nOle hea {1}.kuursuse õpetajaks!".format(kool,kursus))