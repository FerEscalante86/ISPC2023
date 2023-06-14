#numeros mayores y menores de 100

numeros = []

for i in range (10):
        numero = float(input("Ingrese un número:  "))
        numeros.append (numero)
print("Números ingresados:  ", numeros)

cantidad_mayores = 0
cantidad_menores = 0
maximo = max (numeros)
minimo = min (numeros)


for numero in numeros:
    if numero > 100:
	    cantidad_mayores += 1
    else:
        cantidad_menores += 1

print ("Cantidad de números mayores a 100: ", cantidad_mayores)
print ("Cantidad de números menores a 100: ", cantidad_menores)
print ("Número máximo: ", maximo)
print ("Número mínimo: ", minimo)