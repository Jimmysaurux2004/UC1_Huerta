#EJERCICIO5
'''
Conversión de temperatura: Solicita al usuario que ingrese una temperatura en grados Celsius y conviértela a grados Fahrenheit.
'''
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ejemplo de uso
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print("La temperatura en grados Fahrenheit es:", celsius_a_fahrenheit(celsius))
