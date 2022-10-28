#Números compuestos
number = input("Please enter a number: ")
if number.isnumeric():
    number = int (number)
else:
    print ("Error")
aux = number-1
count= 0

if number <= 1:
    print (f"The number {number} no es compuesto")
else:
    while aux > 1:
        if number % aux == 0:
            print ("aux",aux)
            print ("operation", number%aux)
            count += 1
            break
        aux -= 1
    
    if count == 0: 
        print (f"The number {number} no es compuesto")
    else:
        print (f"The number {number} es compuesto")