from CursoEmVideo.modulos.moeda import aulaa

p = float(input("digite o valor do item: "))
print(f"a metade de {aulaa.moeda(p)} e {aulaa.moeda(aulaa.metade(p))}\n"
      f"o dobro de {aulaa.moeda(p)} e {aulaa.moeda(aulaa.dobro(p))}\n"
      f"aumentendo 10%, temos {aulaa.moeda(aulaa.aumentar(p))}\n"
      f"reduzindo 13%, temos {aulaa.moeda(aulaa.diminuir(p))}\n")
