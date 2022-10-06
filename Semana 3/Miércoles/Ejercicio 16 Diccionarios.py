currency_dict = {'euro':'€', 'dollar':'$', 'yen': '¥'}
currency_input = input ("Please enter a currency name eg: euro, dollar, yen: ")

print (currency_dict.get (currency_input.lower(), "Currency not found"))