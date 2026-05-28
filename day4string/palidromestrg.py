# check if a string is a palindrome
str = input("enter the string: ")
if str == str[::-1]:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome") 
