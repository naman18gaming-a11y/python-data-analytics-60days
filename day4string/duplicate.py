text = input("Enter a string: ")
freq = {}

# Step 1: Count frequency of each character
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Step 2: Print duplicates
print("Duplicate characters are:")
for key, value in freq.items():
    if value > 1:
        print(key, "appears", value, "times")
