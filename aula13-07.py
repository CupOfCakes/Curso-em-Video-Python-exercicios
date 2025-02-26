print("="*6 + "NUMERO PRIMO" + "="*6)
n = int(input("qual numero deseja descobrir se e primo? "))

if n % 2 == 0 and n != 2:
    print("não e primo")
elif n % 3 == 0 and n != 3:
    print("não e primo")
elif n % 4 == 0 and n != 4:
    print("não e primo")
elif n % 5 == 0 and n != 5:
    print("não e primo")
elif n % 6 == 0 and n != 6:
    print("não e primo")
elif n % 7 == 0 and n != 7:
    print("não e primo")
else:
    print("\33[36me primo *0*\33[m")
