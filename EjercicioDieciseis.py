#números negativos

for i in range (15):
    numero = float(input("Ingrese un número negativo:  "))
    if numero < 0:
    	numero = abs (numero)
    	print ("El número ingresado convertido en positivo es: ", numero)
    else:
    	print ("El número ingresado no es válido.")