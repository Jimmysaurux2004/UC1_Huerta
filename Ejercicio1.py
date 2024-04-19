def calcular_interes_simple(p, r, t):
    interes = (p * r * t) / 100
    return interes

principal = float(input("Ingrese el monto principal: "))
tasa_interes = float(input("Ingrese la tasa de interés (%): "))
tiempo = float(input("Ingrese el tiempo en años: "))

interes_simple = calcular_interes_simple(principal, tasa_interes, tiempo)
print("El interés simple es:", interes_simple)
