#reverse a number
num = int(input("enter the number:"))
reverse = 0
while num > 00:
    digit = num % 10
    reverse = reverse * 10 + digit
print("the reverse of the number is :", reverse)