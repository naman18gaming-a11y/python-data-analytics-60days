#Count Frequency of Characters
str = input("enter the string:")
freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("the frequency of characters in the string is:")
for key, value in freq.items():
    print(key, ":", value)      