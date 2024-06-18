sectores = ["centro", "colina", "industrias"]
sectorcentro = []
sectorcolina = []
sectorindustria = []


def registrar_pedido(cliente):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    comuna = input("Ingrese comuna: ")
    sector = input("Ingrese su sector (Centro, Colina, Industria): ").lower()
    while sector not in sectores:
        print("Sector no valido, intente otra vez")
        sector = input("Ingrese su sector (Centro, Colina, Industrias): ").lower()

    print("Tenemos disponible cilindros de 5, 15 y 45 kilos, porfavor elegir cuantos necesita de cada uno")
    cil5kg = int(input("Cuantos cilindros de 5kg quiere?: "))
    cil15kg = int(input("Cuantos cilindros de 15kg quiere?: "))
    cil45kg = int(input("Cuantos cilindros de 45kg quiere?: "))

    cliente.append({
        "Cliente" : nombre,
        "Apellido" : apellido,
        "Comuna" : comuna,
        "Sector" : sector,
        "Cil 5kg" : cil5kg,
        "Cil 15kg" : cil15kg,
        "Cil 45kg" : cil45kg
    })

    if sector == "centro":
        sectorcentro.append({
            "Cliente" : nombre,
            "Apellido" : apellido,
            "Sector" : sector,
            "Cil 5kg" : cil5kg,
        "Cil 15kg" : cil15kg,
        "Cil 45kg" : cil45kg

        })
        
    if sector == "colina":
        sectorcolina.append({
            "Cliente" : nombre,
            "Apellido" : apellido,
            "Sector" : sector,
            "Cil 5kg" : cil5kg,
        "Cil 15kg" : cil15kg,
        "Cil 45kg" : cil45kg
        })

    if sector == "industria":
        sectorindustria.append({
            "Cliente" : nombre,
            "Apellido" : apellido,
            "Sector" : sector,
            "Cil 5kg" : cil5kg,
        "Cil 15kg" : cil15kg,
        "Cil 45kg" : cil45kg
        })


def lista_pedidos(cliente):
    print("Lista De Pedidos")
    for pedido in cliente:
        print(pedido)

def hoja_ruta(hojaruta):
    print("Seleccione algun sector")
    print("Centro")
    print("Colina: ")
    print("Industria: ")

    sector_seleccionado = input("Ingrese opción: ")

    if sector_seleccionado == "centro":
        print(sectorcentro)
    else:
        if sector_seleccionado == "colina":
            print(sectorcolina)
        else:
            if sector_seleccionado == "industria":
                print(sectorindustria)
            else:
                if sector_seleccionado == "":
                    print("No hay pedidos en ese sector")









