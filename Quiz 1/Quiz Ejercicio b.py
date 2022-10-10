def main():
    juegos = {
        "Shooter": [
            {
                "id": 1,
                "name": "Overwatch2",
                "price": 60  
            },
            {
                "id": 2,
                "name": "Valorant",
                "price": 0
            },
            {
                "id": 3,
                "name": "Pixel Gun 3D",
                "price": 10
            }
        ],
        "RPG": [
            {
                "id": 4,
                "name": "Pokemon",
                "price": 50  
            },
            {
                "id": 5,
                "name": "Final Fantasy Exvius",
                "price": 0
            }
        ],
        "Open World": [
            {
                "id": 6,
                "name": "Minecraft",
                "price": 60  
            },
            {
                "id": 7,
                "name": "Cyberpunk 2077",
                "price": 60
            },
            {
                "id": 8,
                "name": "GTA V",
                "price": 40
            }
        ],  
    }

    clientes_totales={}
    print ("*****Bienvenido*****")
    while True:
        opciones = input ("Ingrese una opción válida: \n1- Lista de Juegos \n2- Registrar una compra \n3- Estadísticas \n4- Devolver al menú")
        if opciones.isnumeric():
            opciones= int(opciones)
        else:
            print ("Error")
        tipos_de_juego= { 1: "Shooter" , 2: "RPG", 3:"Open World"}
    
        if opciones == 1:
            for tipos_de_juego, categorías  in juegos.items():
                for juego in categorías:
                    id = juegos.get("id")
                    juego_name = juegos.get("name")
                    price = juegos.get ("price")
                    print (f"id: {id}, name; {juego_name} , price: {price}")
                if price == 0:
                    print ("Su juego es gratis")
    
        elif opciones == 2:
            juego_id = input ("Please enter product id: ")
            for tipo_de_juego,categorías in juegos.items():
                for juego in categorías:
                    if juegos.get("id") == juego_id:
                        juego_seleccionado = juegos
                        break
            while True:
                if juego_seleccionado:
                    nombre = input ("Por favor ingrese su nombre y apellido: ")
                    cédula = input ("Por favor ingrese su cédula: ")
                    clientes_totales ["nombre"] = nombre
                    clientes_totales ["cédula"] = cédula
                    clientes_totales ["juego_id"] = juego_id
                    cédula = []
                    if cédula.isnumeric():
                        cédula = int(cédula)
                        aux= cédula - 1
                        count = 0
                        while aux > 1:
                            if cédula % aux == 0:
                                print ("aux", aux)
                                print  ("operation", cédula%aux)
                                cont += 1
                                break
                            aux -= 1
                        print ("Usted tiene un descuento del 40 por ciento")
                juego_seleccionado = None
                print ("******FACTURA******")
                for key, value in clientes_totales.items():
                    if key == juego_id:
                        print("product")
                    print (f"nombre del cliente: {nombre}, cédula: {cédula} , nombre del juego: {juego_name} , price: {price}")
                else:
                    break
        
        elif opciones == 3:
            for clientes, registro in clientes_totales.items():
                 for estadísticas in registro:
                    print (clientes_totales)
                    id_juegos = clientes_totales.get("id")
                    print (clientes_totales.count(id))
        
        elif opciones == 4:
            continue


main()
    
    

            
