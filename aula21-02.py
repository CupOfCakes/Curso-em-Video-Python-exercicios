def fatorial(num, bool=False):
    f = 1
    for c in range(num, 0, -1):
        if bool and num != 1:
            print(f"{num} x ", end="")
        elif bool and num == 1:
            print("1 = ", end="")
        f *= num
        num -= 1

    print(f)


fatorial(5)
