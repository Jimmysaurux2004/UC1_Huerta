#EJERCICIO2
'''
Simulación de lanzamiento de dados: Simula el lanzamiento de dos dados y calcula la suma de los valores obtenidos.
'''
import random

def lanzamiento_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Ejemplo de uso
dado1, dado2 = lanzamiento_dados()
print("Dado 1:", dado1)
print("Dado 2:", dado2)
print("Suma de los dados:", dado1 + dado2)
