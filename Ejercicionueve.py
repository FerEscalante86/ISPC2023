#ejercicionueve

num1 = int(input("Ingresa por favor un primer número "))
num2 = int(input("Ingreso por favor un segundo número "))
num3 = int(input("Ingreso por favor un tercer número "))

if num1>num2 and num1>num3:
    print("El primer número es el mayor")
    if num1 % 2 == 0:
        print("Este número es par")
    else:
    	print("Este número es impar")
elif num2>num1 and num2>num3:
	print("El segundo número es el mayor")
	if num2 % 2 == 0:
		print("Este número es par")
	else:
		print("Este número es impar")
elif num3>num1 and num3>num2:
    print("El tercer número es el mayor")
    if num3 % 2 == 0:
    	print("Este número es par")
    else:
    	print("Este número es impar")
elif num1==num2 and num1==num3:
	print("Los tres números son iguales")