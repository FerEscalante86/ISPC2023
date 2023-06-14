#Edad y sexos

mujeres = 0
hombres = 0
mayores = 0
menores = 0

for i in range (15):
    edad = int(input("Ingrese la edad de la persona:  "))
    sexo = input ("Ingrese el sexo de la persona:  ")

    if sexo == "femenino" or sexo == "mujer":
    	mujeres += 1
    elif sexo == "masculino" or sexo == "hombre":
        hombres += 1

    if edad > 17:
    	mayores += 1
    else:
    	menores += 1


print ("Cantidad de mujeres: ", mujeres)
print ("Cantidad de hombres: ", hombres)
print ("Cantidad de mayores de edad: ", mayores)
print ("Cantidad de menors de edad: ", menores)

