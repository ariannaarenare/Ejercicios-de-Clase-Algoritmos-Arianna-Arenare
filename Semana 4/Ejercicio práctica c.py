
infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db={}

print ("****WELCOME****")
options = input ("Please enter a valid option: \n1: Choque, \n2: Semáforo, \n3: Falta de documentos ")
if options.isnumeric():
    options = int (options)
else:
    print ("Error")

    