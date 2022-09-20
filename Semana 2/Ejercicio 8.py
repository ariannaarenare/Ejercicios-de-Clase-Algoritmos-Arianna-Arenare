print("Welcome to Bella Napoli")
option = input("Please enter an option: \n1-Vegetarian\n2-Non Vegetarian")
if option.isnumeric():
    option=int(option)
    if option == 1:
        ingredient = input("Please enter an ingredient: \n1-Pimiento\n2-Tofu")
        if ingredient =="1":
            ingredient= "Pimiento"
        else:
            ingredient= "Tofu"
        print ("The pizza is vegetarian and have")


    elif option == 2:
        ingredient = input("Please enter an ingredient: \n1-Pepperoni\n2-Jamón\n3-Salmón")
        if ingredient =="1":
            ingredient="Pepperoni"
        elif ingredient== "2":
            ingredient= "Jamón"
        else:
            ingredient= "Salmón"
else:
    print("Error")
