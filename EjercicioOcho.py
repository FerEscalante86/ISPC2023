#EjercicioOcho

precio_de_lista= int(input("Ingrese el precio de su producto: "))
forma_de_pago= int(input("Ingrese el número de la forma de pago que haya elegido:\n 1.Contado \n 2.Tarjeta \n 3.Débito \n "))

if forma_de_pago == 1:
    descuento = precio_de_lista / 10
    importe_total = precio_de_lista - descuento
    print("Importe: $", precio_de_lista)
    print("Descuento: $", descuento)
    print("Importe a pagar: $", importe_total)

elif forma_de_pago == 2:
    recargo = precio_de_lista / 10
    importe_total = precio_de_lista + recargo
    print("Importe: $", precio_de_lista)
    print("Recargo: $", recargo)
    print("Importe a pagar: $", importe_total)

elif forma_de_pago == 3:
    descuento = precio_de_lista / 20
    importe_total = precio_de_lista - descuento
    print("Importe: $", precio_de_lista)
    print("Descuento: $", descuento)
    print("Importe a pagar: $", importe_total)