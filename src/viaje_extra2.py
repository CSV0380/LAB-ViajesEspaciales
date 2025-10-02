

##### EJERCICIO 1


distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24

semanas = int(tiempo_dias) // 7
dias_restantes = int(tiempo_dias) % 7

print(f"Tardarías {semanas} semanas y {dias_restantes} días en llegar.")



##### EJERCICIO 2


distancia_km = int(input("Elige la distancia: "))
velocidad_kmh = int(input("Elige la velocidad: "))

tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24

semanas = tiempo_dias // 7
dias_restantes = tiempo_dias % 7

print(f"Tardarías {semanas} semanas y {dias_restantes} días en llegar.")



##### EJERCICIO 3 (No hay datos de días)



##### EJERCICIO 4


distancia_km = 225_000_000

for velocidad in range(10000, 50001, 10000):
    tiempo_horas = distancia_km / velocidad
    tiempo_dias = tiempo_horas / 24
    semanas = int(tiempo_dias) // 7
    dias_restantes = int(tiempo_dias) % 7
    print(f"Velocidad: {velocidad} km/h -> {semanas} semanas y {dias_restantes} días")



##### EJERCICIO 5


def tiempo_en_llegar():
    distancia = int(input("Elige la distancia: "))  
    velocidad = int(input("Elige la velocidad: "))
    tiempo_horas = distancia / velocidad
    tiempo_dias = tiempo_horas / 24

    semanas = int(tiempo_dias) // 7
    dias_restantes = int(tiempo_dias) % 7

    print(f"Tardarías {semanas} semanas y {dias_restantes} días en llegar.")


if __name__ == "__main__":
    while True:
        tiempo_en_llegar()
        otra = input("¿Quieres hacer otra simulación? (s/n): ").lower()
        if otra != "s":
            print("Programa terminado.")
            break
