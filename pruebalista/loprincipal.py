import funcion as fn
cliente = []
hojaruta = []


while True:
    print("Bienvenido a Gaxplosive, reparto de cilindros")
    print("**********************************************")
    print("1. Registrar pedido")
    print("2. Listar los todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        fn.registrar_pedido(cliente)

    else:
        if opcion == 2:
            fn.lista_pedidos(cliente)

        else:
            if opcion == 3:
               fn.hoja_ruta(hojaruta)
            else: 
                if opcion == 4:
                    print("Gracias por preferir Gaxplosive :)")
                    break


    

