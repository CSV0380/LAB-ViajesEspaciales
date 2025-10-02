distancia_km = int(input("Elige la distancia: "))  # distancia Tierra - Luna
velocidad_kmh = int(input("Elige la velocidad: "))

tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")