def main():
    number1 = input ("Please enter a number: ")
    number2 = input ("Please enter a second number: ")
    aux = number1-1
    aux2= number2 -1
    acum = 0
    acum2 = 0
    divisores_number1 = {}
    divisores_number2 = {}

    if number1.isnumeric():
        number1 = int(number1)
    else: 
        print ("Error")

    if number2.isnumeric():
        number2 = int(number2)
    else:
        print ("Error")

        while aux >= 1:
            if number1 % aux==0:
                acum += aux
            aux -=1
        #print (acum)
 
        while aux >= 1:
            if number2 % aux==0:
                acum2 += aux
            aux2 -=1
        #print (acum2)

        if acum == number2 and acum2 == number1:
            print (f"The numbers {number1} and {number2} are friends")
        else:
            print (f"The numbers {number1} and {number2} are not friends")






main()