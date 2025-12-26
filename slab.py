unit=float(input("Enter total unit:"))
bill= 0
if unit<=100:
    bill= unit*1
elif unit<=200:
    bill= (100*1) + (unit - 100)*2
else:
    bill= (100*1) + (100*2) + (unit-200)*3
    
print("Total electricity bill= ", bill)