n = int(input("qual numero deseja saber a tabuada?: "))
m = 1

while True:
    while m != 11:
        print(f"{n} X {m} = {n*m}")
        m += 1
    print("-=" * 30)
    m = 1
    print(">se quiser terminar o programa digite 0 ou inferior")
    n = int(input("qual numero deseja saber a tabuada?: "))
    if n <= 0:
        break
