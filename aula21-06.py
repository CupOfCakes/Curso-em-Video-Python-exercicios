def helpizinho(msg):
    print(f"\33[36mmanual de {msg}\33[m")
    print(f"\33[30m{help(msg)}")


r = str(input("\33[32mfunção ou biblioteca, digite fim se quiser terminar: \33[m")).lower()
while r != "fim":
    helpizinho(r)
    r = str(input("\33[32mfunção ou biblioteca, digite fim! se quiser terminar: \33[m")).lower()

print("\33[31mfim\33[m")
