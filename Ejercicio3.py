#EJERCICIO3
'''
Cálculo de la velocidad media: Solicita al usuario que ingrese la distancia recorrida y el tiempo transcurrido, y calcula la velocidad media.
'''
def velocidad_media(distancia, tiempo):
    return distancia / tiempo

# Ejemplo de uso
distancia = float(input("Ingrese la distancia recorrida (en metros): "))
tiempo = float(input("Ingrese el tiempo transcurrido (en segundos): "))
print("La velocidad media es:", velocidad_media(distancia, tiempo), "m/s")
