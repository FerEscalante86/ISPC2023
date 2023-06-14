#numeros positivos

suma_positivos = 0

for i in range (10):
    numero = float(input("Ingrese un número:  "))
    if numero > 0:
    	suma_positivos += numero
    	print (numero)
    elif numero < 0:
    	print ("Es un número negativo")
print ("La suma de los números positivos ingresados es: ", suma_positivos)