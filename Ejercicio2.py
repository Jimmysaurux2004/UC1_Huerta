def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 7
if es_par(numero):
    print(numero, "es par")
else:
    print(numero, "es impar")
