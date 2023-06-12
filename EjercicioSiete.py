#EjercicioSiete

print("Para saber si el triángulo es isósceles, escaleno o equilátero")
lado1= input("Ingrese un lado de su triágnulo ")
lado2= input("Ingrese otro lado de su triángulo ")
lado3= input("Ingrese el tercer lado de su triángulo ")

if lado1 == lado2 == lado3:
    print("Su triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Su triángulo es isósceles")
else:
    print("Su triángulo es escaleno")
