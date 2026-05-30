import re

password = input("Enter a password: ")
score = 0

# Rule 1: Length
if len(password) >= 8:
    score += 1

# Rule 2: Uppercase
if re.search(r'[A-Z]', password):
    score += 1

# Rule 3: Digit
if re.search(r'\d', password):
    score += 1

# Rule 4: Special character
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    score += 1

# Final decision
if score == 4:
    print("Strong password")
elif score == 3:
    print("Moderate password")
elif score == 2:
    print("Weak password")
else:
    print("Very weak password")
