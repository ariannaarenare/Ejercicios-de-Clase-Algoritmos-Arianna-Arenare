age = input("Insert your age")
if age .isnumeric():
    age= int(age)
else:
    print ("Error")

if age >= 18:
    print("Mayor de edad")

if age < 18:
    print("Menor de edad")
