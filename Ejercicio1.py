#EJERCICIO1
'''
Cálculo del promedio ponderado: Solicita al usuario que ingrese las notas y los pesos de varios elementos 
(por ejemplo, exámenes, tareas) y calcula el promedio ponderado.
'''
def promedio_ponderado(notas, pesos):
    suma = sum(nota * peso for nota, peso in zip(notas, pesos))
    total_pesos = sum(pesos)
    return suma / total_pesos if total_pesos != 0 else 0

# Ejemplo de uso
notas = [float(input("Ingrese la nota {}: ".format(i + 1))) for i in range(3)]
pesos = [float(input("Ingrese el peso para la nota {}: ".format(i + 1))) for i in range(3)]
print("El promedio ponderado es:", promedio_ponderado(notas, pesos))
