data_dict = { }
while True:
    data_key= input ("Please enter the data you want to save: ")
    data_value= input ("Please enter the value you want to save: ")
    data_dict [data_key] = data_value

    for key, value in data_dict.items():
        print (f"Your {key} is {value}")

    if input ("Do you want to exit: \n Y-Yes \n N-No") == "Y":
        break