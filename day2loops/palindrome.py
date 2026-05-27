# palindrome in python
num =  int(input("enter the number:"))
temp = num
reverse = 0 
while temp > 0:
    digit = temp % 10
    reverse = digit * 10 + reverse
    temp = temp // 10
    
    if num == reverse:
        print("the number is palindrome")      
    else:
        print("the number is not palindrome")