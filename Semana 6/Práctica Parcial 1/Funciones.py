#Ejemplo
def volumen_cilindro (altura,radio):
    pi = 3.14159
    return altura * pi * radio**2

print (volumen_cilindro(3,10))


#Función de Bienvenida
def bienvenida():
    print ("****BIENVENIDO****")

#Función de opciones al cliente en un diccionario
def opcion(dict):
    for clave, valor in dict.items():
        for clave_interna, valor_interno in valor.items():
            print (f"{clave}-{valor_interno}", end ="")
        print ("")
    return input ("Ingrese una opción: ")

#Función de datos del cliente
def get_client_data(study):
    client= {
        "id": input ("Please enter the client id: "),
        "age":input ("Please enter the client age:"),
        "gender":input ("Please enter the client M or F"),
        "study": study
    }
    return client

#Función para Factura
def print_invoice (client):
    print ("****RECEIPT****")
    print ("ID:", client.get("id"))
    print ("Age:", client.get("age"))
    print ("Gender:", client.get("gender"))
    print ("NetAmount:", client.get("id"))