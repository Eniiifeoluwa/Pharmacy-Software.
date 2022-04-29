print("""----------------------------------------------------------------
     WELCOME TO AKINOLA\'S PHARMACY
------------------------------------------------------------------""")
drugs =["paracetamol",
        "blood capsule",
        "lumartem",
        "amoxillin",
        "silicone gel"]
amount = {
    'paracetamol' : 250,
    'blood capsule' : 230,
    'lumartem' : 140,
    'amoxillin' : 200,
    'silicone gel': 2500
}
print("LISTED BELOW ARE THE DRUGS WE HAVE: \n" + str((drugs)))
drug_name = input("Enter the name of the drug you want to buy: ")
if drug_name in drugs:
    print(drug_name + " is " + str(amount[drug_name]) + " Naira.")
    customer_pin = input("Enter  your ATM pin: ")
    if len(customer_pin) == 4:
        balance = int(input("Enter the amount in your wallet: "))
        print("You have " + str(balance) + " Naira in your wallet.")
        first_number = int(input("Enter the quantity of the drugs: "))
        second_number = str(amount[drug_name])
        operation = int(first_number) * int(second_number)
        if balance < operation:
            print("You are not eligible to buy the drug. Thank you!")
        else:
            print("You can proceed to get the drugs, thanks for patronizing us!")
            print("The total amount is " + str(operation) + " Naira, please visit the pharmacist to have your drugs." )
    else:
        print("You have entered an incorrect pin.")
else:
    print("We do not have what you just requested for, please try the nearest store.")


