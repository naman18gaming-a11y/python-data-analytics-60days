#Remove Spaces
str = input("enter the string:")
newstr = ""
for i in str:
    if i != " ":
        newstr += i
print("the string without spaces is:", newstr)