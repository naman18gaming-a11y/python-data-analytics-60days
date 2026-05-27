# electricity bill counter 
power = float(input("enter the power consumed in unit:"))
time = float(input("enter the time in hours:"))
bill = (power * time)/1000
print("the electricity bill is :", bill)