#EJERCICIO4
'''
Cálculo del área de un círculo: Solicita al usuario que ingrese el radio de un círculo y calcula su área.
'''
import math

def area_circulo(radio):
    return math.pi * radio ** 2

# Ejemplo de uso
radio = float(input("Ingrese el radio del círculo: "))
print("El área del círculo es:", area_circulo(radio))
