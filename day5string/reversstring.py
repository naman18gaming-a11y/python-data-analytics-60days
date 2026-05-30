#Reverse Each Word
int = input("enter the string:")
words = int.split()
rev_words = [word[::-1] for word in words]
rev_str = " ".join(rev_words)
print("the string with each word reversed is:", rev_str)