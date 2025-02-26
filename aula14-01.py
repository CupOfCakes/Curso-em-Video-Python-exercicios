s = str(input("qual o seu genero?[F/M]: ")).upper().strip()[0]

while s not in "MF":
    print("insira um dado valido")
    s = str(input("qual o seu genero?[F/M]: ")).upper().strip()

if s == "M":
    print("you are a man, awesome")
elif s == "F":
    print("you are a woman, beautiful")
