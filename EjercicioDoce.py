#números pares e impares y su suma

while True:
    pares = 0
    suma_de_pares = 0

    for i in range (1 , 5 ):
        numero = int(input(f"Ingrese el número {i} de 4:  "))

        if numero %2 == 0:
            pares += 1
            suma_de_pares += numero
    impares = 4 - pares

    print ("Cantidad de números pares:  ", pares)
    print ("Cantidad de números impares: ", impares)
    print ("Sumatoria de números pares: ", suma_de_pares)
