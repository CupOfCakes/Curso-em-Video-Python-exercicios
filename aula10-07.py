s = float(input("qual o seu salario? "))

if s > 1250.00:
    print("seu salario reajustado e {:.2f}".format(s*1.10))
else:
    print("seu salario reajustado e {:.2f}".format(s*1.15))
