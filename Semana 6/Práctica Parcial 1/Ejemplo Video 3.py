nombre = str(input ("Ingrese su nombre: "))
veces = input ("Ingrese el número de veces que quiere que se repita: ")
if veces.isnumeric():
    veces = int (veces)
else:
    print ("Error")
cont= 0

while cont < veces:
    print (nombre)
    cont += 1




