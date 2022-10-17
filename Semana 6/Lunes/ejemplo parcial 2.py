def is_prime(rif):
    number = int(rif[len(rif)-1])
    cont = 0
    aux= number - 1
    while number > 1:
        if number % aux ==0:
            return False
        aux-= 1 
    return True



def main():
    products= {
        "Q": {
            "name": "Quimico",
            "price":1000
        },
        "F": {
            "name": "Farmaceutico",
            "price":2500
        }, 
        "B": {
            "name": "Biologico",
            "price":4000}}

    client_f =0
    client_q = 0
    client_b= 0
    discount_c =0
    discount_r =0
    rif_max= 0
    max_purchase = 0
    total_day= 0

    while True: 
        rif = input ("Please enter your rif: ")
        type_payment = input ("Please enter your payment type: \nC - One time \nR- Credito \n  ")
        product_code = input ("Please enter the product code: \nQ - Quimico \nF- Farmaceutico \nB- Biologico")
        discount = 0
        tax= 0
        gross_amount = products.get (product_code).get("price")
        
        #Discounts
        if type_payment == "C":
            discount += gross_amount * 0.03
        if gross_amount % 2 == 0:
            discount += 0.02
        if is_prime(rif):
            discount += gross_amount * 0.05
        #Taxes
        if product_code != "F":
            tax += gross_amount * 0.12
        #Total
        total = gross_amount + tax - discount

        
        #Final Data
        if product_code == "F":
            client_f += 1
        elif product_code == "Q":
            client_q += 1
        elif product_code == "B":
            client_b += 1

        if type_payment == "C":
            discount_c += discount
        elif type_payment == "R":
            discount_r += discount

        if total > max_purchase:
            rif_max = rif
            max_purchase = total

        total_day += total

        #Factura
        print ("****RECEIPT****")
        print ("RIF: ",rif)
        print ("PRODUCT: ",products.get (product_code).get("name"))
        print ("PAYMENT METHOD: ",type_payment)
        print ("TAX: ",tax)
        print ("DISCOUNT: ",discount)
        print ("TOTAL", total)
        

        if input ("Do you wnat to exit: Y- YES - N-NO: ") == "Y":
            break
    print ("****END OF THE DAY****")
    print ("Clients F:", client_f)
    print ("Clients B:",client_b)
    print ("Client Q: ",client_q)
    print ("Discount Credit:", discount_r)
    print ("Discount for one time purchase:", discount_c)
    print ("Rif maxium purchase:", rif_max)
    print ("Total day:",total_day)







main()