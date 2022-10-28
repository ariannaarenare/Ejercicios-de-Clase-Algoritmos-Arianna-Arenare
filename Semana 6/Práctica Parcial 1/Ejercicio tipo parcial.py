def bienvenida():
    print ("****BIENVENIDO****")

def opcion(dict):
    for clave, valor in dict.items():
        for clave_interna, valor_interno in valor.items():
            print (f"{clave}-{valor_interno}", end ="")
        print ("")
    return input ("Ingrese una opción: ")

def cliente_datos(vehiculo):
    cliente = {
        "cedula": input ("Ingrese su cedula: "),
        "tipo de vehiculo": vehiculo,
        "horas": input ("Ingrese el número de horas que manejo: ")
    }
    return cliente



def factura(cliente):
    print ("****FACTURA****")
    print ("cedula", cliente.get("cedula"))
    print ("vehiculo", cliente.get("tipo de vehiculo"))
    print ("monto neto", cliente.get("horas"))

#def monto_neto(cliente):

def main():
    tipo_de_vehiculo = {
        "A":{"name":"automatico",
        "precio":2500},
        "S":{"name":"sincronico",
        "precio":3500}
        }

    bienvenida()
    clientes = []
    while True:
        opciones = opcion(tipo_de_vehiculo)
        cliente = cliente_datos(opciones)

        factura(cliente)
        clientes.append(cliente)

main()