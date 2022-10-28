a= 0
b=1
c= a+b

limite = input ("Ingrese un número de límite para la secuencia: ")
if limite.isnumeric():
    limite = int(limite)
else: 
    print ("Error")

while c < limite:
    while c == 0:
        print (a)
        a= c
        c=a
        break
    print (c)
    break