print()
print("Compound Interest Calculator")
print()
amount = float(input("Input the amount of money: £"))
years  = int(input("Input the amount of years you will like to invest: "))
interestrate = float(input("Input the compund interest rate (in %):  "))
print()

titleYears = "YEARS"
titleAmount = "START AMOUNT"
titleInterestRate = "INTEREST RATE"
titleInterest = "INTEREST"
titleFINAL = "FINAL"

def numformat(num):
    return ("{:,}".format(num))

y = 1

print("%-7s  %-15s  %-15s  %-15s  %-15s" %(titleYears,titleAmount,titleInterestRate,titleInterest,titleFINAL))

interest = amount * interestrate/100
final = amount + interest
print("%-7s  %-15s  %-15s  %-15s  %-15s" % (y, numformat(round(amount)), interestrate, numformat(round(interest,2))    ,numformat(round(final,2))))
y = y + 1

for x in range(years - 1 ):
    amount = final
    interest = amount * interestrate/100
    final =  amount + interest
    print("%-7s  %-15s  %-15s  %-15s  %-15s" %(y  ,numformat(round(amount,2))  ,interestrate,     numformat(round(interest,2))      ,numformat(round(final,2))))
    y = y + 1

print()
print("You will have £",numformat(round(final,2)),"at the end of",years,"years.")