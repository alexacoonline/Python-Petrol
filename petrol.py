#  python code for petrol
def calcPrice(litre,ppltr):
    amount = litre * ppltr
    return amount


def calcLitre(price,ppltr):
    litre = price/ppltr
    return litre


ppl = float(input("Enter Amount per Litre"))
print("Select Your Purchase Preference")
print("1: Price")
print("2: Litres")
choice = int(input(""))
if choice == 1:
    amt = float(input("Enter the Amount of Petrol you want to buy"))
    print("You bought ", calcLitre(amt, ppl), " Litres")
elif choice == 2:
    lit = float(input("Enter the Quantity of Petrol you want to buy in Litres"))
    print("You bought ", calcPrice(lit, ppl), " worth of Petrol")

exits = input("press 0 to exit")[0]
if exits == 0:
    exit()


