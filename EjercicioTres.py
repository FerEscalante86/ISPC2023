#tercerejercicio

print("Información sobre mesas por género")
genero= input("Por favor ingrese ´f´ minúscula o ´m´ minúscula según su género  ")

if genero == "f":
    print("Usted debe votar en mesa Femenina ")
elif genero == "m":
    print("Usted debe votar en mesa Masculina ")
elif genero == "F":
    print("Por favor asegúrese que ´f´ o ´m´ sean  minúsculas ")
elif genero == "M":
    print("Por favor asegúrese que ´m´ o ´f´ sean  minúsculas ")
else:
    print("Ha ocurrido un error. Por favor vuelva a ingresar ´f´ minúscula o ´m´ minúscula según su género ")