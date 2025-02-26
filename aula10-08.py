print("======E UM TRINAGULO?======")
n1 = float(input("qual o valor da 1 reta: "))
n2 = float(input("qual o valor da 2 reta: "))
n3 = float(input("qual o valor da 3 reta: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("\33[0:33mITS A  FUCKING TRIANGULO OMG *0*\33[m")
else:
    print("não e um trinagulo :(")
