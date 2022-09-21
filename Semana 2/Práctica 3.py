number1 = input ("Insert number1")
if number1 .isnumeric():
    number1 =float(number1)
else:
    print("Error")

number2 = input ("Insert number2")
if number2 .isnumeric():
    number2 =float(number2)
else:
    print("Error")

if number1/number2 == 0:
    print ("Error")
else:
    print (number1/number2)