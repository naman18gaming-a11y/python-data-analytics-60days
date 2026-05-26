# Simple Interest Calculator

# Taking input from user
x = float(input("Enter Principal amount: "))
y = float(input("Enter Rate of Interest: "))
z = float(input("Enter Time (in years): "))

# Formula for Simple Interest
SI = (x * y * z) / 100

# Output
print("The value of simple interest is:", SI)
