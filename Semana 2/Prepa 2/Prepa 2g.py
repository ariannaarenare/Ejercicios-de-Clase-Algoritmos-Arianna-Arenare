estudiantes = ["Jesús", "Alejandro", "Ana","Sergio"]


nombre = "Pablo"
estudiantes.insert(0, nombre)

estudiantes.remove("Sergio")
for estudiante in estudiantes:
    print (estudiante)