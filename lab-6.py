name= input("Enter your name: ")
age= int(input("Enter your age: "))
membership= input("Are you a member? ")

if age <=18:
    if membership == "yes":
        print("Your payment is 450.00 pesos")
    if membership == "no":
        print("Your payment is 650.00 pesos")
if age >=19 and age <=65:
    if membership == "yes":
        print("Your payment is 550.00 pesos")
    if membership == "no":
        print("Your payment is 750 pesos")
if age >=66:
    if membership == "yes":
        print("Your payment is 400 pesos")
    if membership == "no":
        print("Your payment is 600 pesos")
            
    