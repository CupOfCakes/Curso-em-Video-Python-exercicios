def voto(a):
    from datetime import date
    n = date.today().year - a
    return n


r = int(input("qual ano vc nasceu?: "))
n = voto(r)
if n < 16:
    print(f"com {n} ano não vota")
elif 18 <= n < 65:
    print(f"com {n} o voto e obrigatorio")
else:
    print(f"com {n} o voto e opcional")
