def puedes_viajar(edad, nivel_fisico):
    if edad < 18:
        print("Debes ser mayor de edad")
    elif nivel_fisico < 5:
        print("Debes estar en mejor forma")
    else:
        print("¡Listo para despegar!")


if __name__ == "__main__":
    edad = int(input("Dime tu edad: "))
    nivel_fisico = int(input("Dime tu estado fisico: "))
    puedes_viajar(edad, nivel_fisico)



"""
# O bien:

def puedes_viajar(edad, nivel_fisico):
    if edad < 18:
        return "Debes ser mayor de edad"
    elif nivel_fisico < 5:
        return "Debes estar en mejor forma"
    else:
        return "¡Listo para despegar!"
    


if __name__ == "__main__":
    edad = int(input("Dime tu edad: "))
    nivel_fisico = int(input("Dime tu estado fisico: "))
    resultado = puedes_viajar(edad, nivel_fisico)
    print(resultado)

"""


