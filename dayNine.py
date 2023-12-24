myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
myTip = int(input("What percentage of tip would you like to leave? "))
myTip /= 100
myTotal = myTip * myBill
myTotal += myBill
myTotal /= numberOfPeople
print("Okay, you each have to pay", myTotal)