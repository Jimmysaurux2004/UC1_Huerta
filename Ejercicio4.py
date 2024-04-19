def numeros_pares(limite):
    pares = []
    for i in range(2, limite+1, 2):
        pares.append(i)
    return pares

limite = 10
print("Números pares hasta", limite, ":", numeros_pares(limite))
