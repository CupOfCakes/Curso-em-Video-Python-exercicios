from time import sleep

for c in range(10, -1, -1):
    print(c)
    if c != 0:
        sleep(1)
print("\33[35mOS FOGOS ESTOURARAM\33[m")
