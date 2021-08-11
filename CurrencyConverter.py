
def numformat(num):
    return ("{:,}".format(num))

def pound():

    amount = int(input("How much money do you want to convert:  £: "))
    print("Which currency would you like to convert your money into: ")

    print()
    print("1.Euro")
    print("2.US Dollars")
    print("3.Nigerian Naira")
    print("4.Chinese Yuan")
    print("5.Japanese Yen")
    print()


    euro_amount = amount * 1.16
    dollars_amount = amount * 1.39
    naira_amount = amount * 575.62
    yuan_amount = amount * 9.06
    yen_amount = amount * 155.01

    currency = int(input())

    if currency == 1:
        print("£", amount, "in Euros is €", numformat(round(euro_amount, 3)))
    elif currency == 2:
        print("£", amount, "in US Dollars is $", numformat(round(dollars_amount, 3)))
    elif currency == 3:
        print("£", amount, "in Nigerian Naira is ₦", numformat(round(naira_amount, 3)))
    elif currency == 4:
        print("£", amount, "in Chinese Yuan is ¥", numformat(round(yuan_amount, 3)))
    elif currency == 5:
        print("£", amount, "in Japanese Yen is  ¥", numformat(round(yen_amount, 3)))

def dollar():

    amount = int(input("How much money do you want to convert:  $: "))
    print("Which currency would you like to convert your money into: ")

    print()
    print("1.Euro")
    print("2.Pound")
    print("3.Nigerian Naira")
    print("4.Chinese Yuan")
    print("5.Japanese Yen")
    print( )

    euro_amount = amount * 0.85
    pound_amount = amount * 0.72
    naira_amount = amount * 411.59
    yuan_amount = amount * 6.49
    yen_amount = amount * 110.60

    currency = int(input())

    if currency == 1:
        print("$", amount, "in Euros is €", numformat(round(euro_amount, 3)))
    elif currency == 2:
        print("$", amount, "in Pound Sterling is $", numformat(round(pound_amount, 3)))
    elif currency == 3:
        print("$", amount, "in Nigerian Naira is ₦", numformat(round(naira_amount, 3)))
    elif currency == 4:
        print("$", amount, "in Chinese Yuan is ¥", numformat(round(yuan_amount, 3)))
    elif currency == 5:
        print("$", amount, "in Japanese Yen is  ¥", numformat(round(yen_amount, 3)))

def naira():
    amount = int(input("How much money do you want to convert:  ₦: "))
    print("Which currency would you like to convert your money into: ")

    print()
    print("1.Euro")
    print("2.Pound")
    print("3.US Dollar")
    print("4.Chinese Yuan")
    print("5.Japanese Yen")
    print()

    euro_amount = amount * 0.0021
    pound_amount = amount * 0.0018
    dollar_amount = amount * 0.0024
    yuan_amount = amount * 0.016
    yen_amount = amount * 0.27

    currency = int(input())

    if currency == 1:
        print("₦", amount, "in Euros is €", numformat(round(euro_amount, 3)))
    elif currency == 2:
        print("₦", amount, "in Pound Sterling is £", numformat(round(pound_amount, 3)))
    elif currency == 3:
        print("₦", amount, "in US Dollars is $", numformat(round(dollar_amount, 3)))
    elif currency == 4:
        print("₦", amount, "in Chinese Yuan is ¥", numformat(round(yuan_amount, 3)))
    elif currency == 5:
        print("₦", amount, "in Japanese Yen is  ¥", numformat(round(yen_amount, 3)))

def yuan():

    amount = int(input("How much money do you want to convert:  ¥: "))
    print("Which currency would you like to convert your money into: ")

    print()
    print("1.Euro")
    print("2.Pound")
    print("3.US Dollar")
    print("4.Nigerian Naira")
    print("5.Japanese Yen")
    print()

    euro_amount = amount * 0.13
    pound_amount = amount * 0.11
    dollar_amount = amount * 0.15
    naira_amount = amount * 63.46
    yen_amount = amount * 17.05

    currency = int(input())

    if currency == 1:
        print("¥", amount, "in Euros is €", numformat(round(euro_amount, 3)))
    elif currency == 2:
        print("¥", amount, "in Pound Sterling is £", numformat(round(pound_amount, 3)))
    elif currency == 3:
        print("¥", amount, "in US Dollars is $", numformat(round(dollar_amount, 3)))
    elif currency == 4:
        print("¥", amount, "in Nigerian Naira is ₦", numformat(round(naira_amount, 3)))
    elif currency == 5:
        print("¥", amount, "in Japanese Yen is  ¥", numformat(round(yen_amount, 3)))

def yen():

    amount = int(input("How much money do you want to convert:  ¥: "))
    print("Which currency would you like to convert your money into: ")

    print()
    print("1.Euro")
    print("2.Pound")
    print("3.US Dollar")
    print("4.Nigerian Naira")
    print("5.Chinese Yuan")
    print()

    euro_amount = amount * 0.0077
    pound_amount = amount * 0.0065
    dollar_amount = amount * 0.0090
    naira_amount = amount * 3.72
    yuan_amount = amount * 0.059

    currency = int(input())

    if currency == 1:
        print("¥", amount, "in Euros is €", numformat(round(euro_amount, 3)))
    elif currency == 2:
        print("¥", amount, "in Pound Sterling is £", numformat(round(pound_amount, 3)))
    elif currency == 3:
        print("¥", amount, "in US Dollars is $", numformat(round(dollar_amount, 3)))
    elif currency == 4:
        print("¥", amount, "in Nigerian Naira is ₦", numformat(round(naira_amount, 3)))
    elif currency == 5:
        print("¥", amount, "in Chinese Yuan is  ¥", numformat(round(yuan_amount, 3)))

def euro():

    amount = int(input("How much money do you want to convert:  €: "))
    print("Which currency would you like to convert your money into: ")

    print()
    print("1.Japanese Yen")
    print("2.Pound Sterling")
    print("3.US Dollar")
    print("4.Nigerian Naira")
    print("5.Chinese Yuan")
    print()

    yen_amount = amount * 129.58
    pound_amount = amount * 0.85
    dollar_amount = amount * 1.17
    naira_amount = amount * 482.30
    yuan_amount = amount * 7.60

    currency = int(input())

    if currency == 1:
        print("€", amount, "in Japanese Yen is ¥", numformat(round(yen_amount, 3)))
    elif currency == 2:
        print("€", amount, "in Pound Sterling is £", numformat(round(pound_amount, 3)))
    elif currency == 3:
        print("€", amount, "in US Dollars is $", numformat(round(dollar_amount, 3)))
    elif currency == 4:
        print("€", amount, "in Nigerian Naira is ₦", numformat(round(naira_amount, 3)))
    elif currency == 5:
        print("€", amount, "in Chinese Yuan is  ¥", numformat(round(yuan_amount, 3)))

#£$₦¥

print("CURRENCY CONVERTER")

def CC():

    print("Enter the name of the currency you currently have: ")
    ccurrency = input()

    if ccurrency.lower() == "pound":
        pound()
    elif ccurrency.lower() == "dollar":
        dollar()
    elif ccurrency.lower() == "naira":
        naira()
    elif ccurrency.lower() == "yuan":
        yuan()
    elif ccurrency.lower() == "yen":
        yen()
    elif ccurrency.lower() == "euro":
        euro()
    else:
        CC()

CC()