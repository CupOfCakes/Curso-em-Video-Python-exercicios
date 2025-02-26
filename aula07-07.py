print("======quanta tinta vai usar?======")
l = float(input("qual a largura da parede? "))
a = float(input("qual a altura da parede? "))
area = l * a
print("você vai precisar de {:.1f}L de tinta".format(area/2))
