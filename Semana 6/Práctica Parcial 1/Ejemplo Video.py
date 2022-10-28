valor1 = input ("Introduce un valor: ")
if valor1.isnumeric():
    valor1 = int (valor1)
else:
    print ("Error")

valor2 = input ("Introduce un segundo valor: ")
if valor2.isnumeric():
    valor2 = int (valor2)
else:
    print ("Error")

resultado = valor1 + valor2

print (f"El resultado es: {resultado}")