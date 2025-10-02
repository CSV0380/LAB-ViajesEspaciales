distancia_km = 225_000_000  

for velocidad in range(10000, 50001, 10000): #donde empiezas, donde acabas y de cuanto en cuanto
    tiempo_horas = distancia_km / velocidad
    tiempo_dias = tiempo_horas / 24
    print(f"Velocidad: {velocidad} km/h -> Tardarías {tiempo_dias} días en llegar.")
