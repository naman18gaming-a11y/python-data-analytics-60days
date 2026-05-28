# count vowels in a string
str = input("enter the string:")
count = 0 
vowels = "aeiouAEIOU"
for i in range(len(str)):
    if str[i] in vowels:
        count += 1
print("the number of vowels in the string is:", count)