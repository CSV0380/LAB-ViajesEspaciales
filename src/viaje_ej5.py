


def tiempo_en_llegar():
    distancia = int(input("Elige la distancia: "))  
    velocidad = int(input("Elige la velocidad: "))
    tiempo_horas = distancia / velocidad
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias:.2f} días en llegar.") # el :.2f sirve para poner 2 decimales




if __name__ == "__main__":
    while True:
        tiempo_en_llegar()
        otra = input("¿Quieres hacer otra simulación? (s/n): ").lower()
        if otra != "s":     #condicion para que se acabe el bucle
            print("Programa terminado.")
            break
