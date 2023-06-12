moneda_extranjera = 400
tipo_de_operacion= int(input("Ingrese el número del tipo de operación que desee:\n 1.convertir pesos a dólares \n 2.convertir dólares a pesos \n "))

if tipo_de_operacion == 1:
    pesos= int(input("Ingrese la cantidad de pesos que desea cambiar "))
    cambio_a_dolar = pesos / moneda_extranjera
    print("Usted tiene $ ", cambio_a_dolar )

elif tipo_de_operacion == 2:
    moneda_extranjera= int(input("Ingrese la cantidad de dólares que desea cambiar "))
    cambio_a_pesos= moneda_extranjera * 400 
    print("Usted tiene $" , cambio_a_pesos)
