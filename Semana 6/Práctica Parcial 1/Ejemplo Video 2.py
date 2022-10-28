opcion = input ("Ingrese una opción: \n1 Suma, \n2 Resta, \n3 Multiplicación, \n4 División : ")
if opcion.isnumeric():
    opcion = int (opcion)

if opcion == 1:
    valor1 = int(input ("Ingrese un valor: "))
    valor2 = int(input ("Ingrese un segundo valor: "))
    resultado1 = valor1 + valor2 
    print (f"El resultado es {resultado1}")

elif opcion == 2:
    valor1 = int (input ("Ingrese un valor: "))
    valor2 = int(input ("Ingrese un segundo valor: "))
    resultado2 = valor1 - valor2
    print (f"El resultado es {resultado2}")

elif opcion ==3:
    valor1 = int(input ("Ingrese un valor: "))
    valor2 = int(input ("Ingrese un segundo valor: "))
    resultado3 = valor1 * valor2
    print (f"El resultado es {resultado3}")

else:
    valor1 = int(input ("Ingrese un valor: "))
    valor2 = int(input ("Ingrese un segundo valor: "))
    resultado4 = valor1 // valor2
    print (f"El resultado es {resultado4}")


