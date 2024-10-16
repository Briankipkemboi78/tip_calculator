print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip % would you like to give? '10', '12, or '15?'?\n"))
people = int(input("How many people to split the bill?\n"))

tipPercentage = round((tip / 100) * bill,2)

person_tip = round(tipPercentage / people, 2)

print(f"Each Person should pay: ${person_tip}")