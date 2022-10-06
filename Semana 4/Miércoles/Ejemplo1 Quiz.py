def main():

products = {}
#Diccionario

print ("*****Welcome*****")
while True:
    option = int(input ("Please enter a valid option: \n1- Show Inventary \n2- Make a purchase \n3- Exit \n4- > "))
    available_types = { 1: "mobiles" , 2: "laptops"}
    if option == 1:
        for types,brands in products.items(): #print(brands)
            for brand_name, product_list in brands.items(): #print (product_list)
                print (brand_name)
                for product in product_list:
                    id = product.get("id")
                    product_name = product.get("name")
                    price = product.get ("price")
                    print (f"id: {product.get("id")} , name {product.get("product_name")} , price: {product.get("price")}")
    elif option == 2:
        product_id = input ("Please enter product id: ")
        for types,brands in products.items(): 
            for brand_name, product_list in brands.items(): 
                for product in product_list:
                    if product.get("id") == product_id:
                        product_selected = product
                        break
        if product_selected:
            name = input ("Please enter your name: ")
        id_card = input ("Please enter your id card: ")
        client ={}
        client ["name"] = name
        client ["id_card"] = id_card
        client ["product_id"] = product_id
        product_selected = None
        print ("******RECIPT******")
        for key, value in client.items():
            if key == product_id:
                print("product")
            print (f"id: {id} , name {product_name} , price: {price}")
            else:
                print (f"Your {key} is {value}")
        else:
            print ("Product not found")

    elif option == 3:
        break
    else:
        continue #Break rompe el ciclo y Continue rompe el ciclo pero te lo continúa


main()