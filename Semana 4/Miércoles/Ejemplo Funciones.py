def volumen_cilindro (altura, radio):
    pi = 3.14
    return altura * pi * radio **2

print (volumen_cilindro (10,3))

#Si se le agrega un tercer valor reemplaza el valor que declaraste por el valor que le pusiste nuevo

def plus_one (num):
    print (num+ 1)
result = plus_one (1)
print (type(result))


#Una función puede recibir o devolver una función (Funciones de alto nivel)