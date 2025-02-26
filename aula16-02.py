times = ("Vitória", "Juventude", "Criciúma", "Atlético-GO", "Novorizontino", "Mirassol", "Sport", "Vila Nova", "CRB",
         "Guarani", "Ceará", "Botafogo-SP", "Avaí", "Ituano", "Ponte Preta", "Chapecoense", "Sampaio Corrêa", "Tombense"
         , "Londrina", "ABC",)

print("======ESTASTISTICAS BRASILEIRÃO 2023 - SERIE B======")
print(f"os 5 primeiros colocados foram {times[:5]}")
print("-=" * 50)
print(f"os 4 ultimos colocados foram {times[-4:]}")
print("-=" * 50)
print(f"o nome dos times em ordem alfabetica e {sorted(times)}")
print("-=" * 50)
print(f"o time da Chapecoense esta na posição {times.index("Chapecoense") + 1}")
