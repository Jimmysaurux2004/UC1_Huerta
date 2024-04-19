def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    cuenta = 0
    for letra in cadena:
        if letra in vocales:
            cuenta += 1
    return cuenta

texto = "Hola, ¿cómo estás?"
print("Cantidad de vocales en el texto:", contar_vocales(texto))
