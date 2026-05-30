#Count Digits and Alphabets Separately
int = input("enter the string:")
countdigit = 0
countalpha = 0
for i in range(len(int)):
    if int[i].isdigit():
        countdigit += 1
    elif int[i].isalpha():
        countalpha += 1
print("Digits:", countdigit)
print("Alphabets:", countalpha) 