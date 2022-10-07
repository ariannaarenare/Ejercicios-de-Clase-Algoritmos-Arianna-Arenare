#Número perfecto: todo número natural que es igual a la suma de sus divisores propios (es decir, todos sus divisores excepto el propio número). Por ejemplo, 6 es un número perfecto ya que sus divisores propios son 1, 2, y 3 y se cumple que 1+2+3=6. Los números 28, 496 y 8128 también son perfectos.

print ("****WELCOME****")
number = input ("Please enter a number: ")

if number.isnumeric():
    number = int(number)
else:
    print ("Error")
suma= 0
aux= number-1 

while aux < number:
    if number % aux == 0:
        aux += 1
        print ("aux", aux)
        suma += 1
        print (f"the number {number} is perfect")
    else:
        print (f"the number {number} is not perfect")
        break


