print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Введите целое число => "))))
        break
    except TypeError:
        print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a #c=b=a=453->45->4->0
    paaris=0
    paaritu=0
    while b > 0:
        if b % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        b //=  10  
    #b=0
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0 #c=453 a=453 b=0
    while a > 0:    # a=453 a=45 a=4
        n= a % 10   # n=3   n=5  n=4
        a = a // 10 # a=45  a=4  a=0
        b = b * 10  # b=0   b=30 b=350
        b +=n       # b=3   b=35 b=354
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()
    #c=453
    if c % 2 == 0:
        print(c, " - чётное число. Делим на 2.")
    else:
        print(c, " - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c!= 1:
        if c % 2 == 0:
            c = c / 2
        else:
            c = (3*c + 1) / 2
        print(int(c), end=" ")
    print()
    print("Гипотеза верна")
















from datetime import date


sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: ")))
praegu=date.today().year #2023

if (praegu-sp.year)%10==0:#sp>date(2000,1,1):
    print("Juubel")
else:
    print("-----")