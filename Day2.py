print("Welcome to the tip calculator")
bill=int(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
new_bill=bill+bill*(tip/100)
people=int(input("How many people to split the bill?"))
each=round((new_bill/people),2)
print(f"Each person should pay: ${each}")