from CursoEmVideo.modulos.moeda import aulab

p = float(input("digite o valor do item: "))
print("=" * 30)
print(f"a metade de {aulab.moeda(p)} e {aulab.metade(p, True)}\n"
      f"o dobro de {aulab.moeda(p)} e {aulab.dobro(p, True)}\n"
      f"aumentendo 10%, temos {aulab.aumentar(p, True)}\n"
      f"reduzindo 13%, temos {aulab.diminuir(p, True)}\n")
