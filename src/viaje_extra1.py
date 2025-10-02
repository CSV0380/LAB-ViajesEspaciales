



distancia = int(input("Dime la distancia que quieres recorrer: "))
autonomia = 150000

paradas = 0
for km in range(autonomia, distancia + 1, autonomia): # range(inicio, fin+1, paso)
    print(f"Parada en el km {km}")
    paradas += 1

print(f"Total de paradas para repostar: {paradas}")
