# password retry system
password = 12345
print("welcome to the password retry system")
attempts = 3
while attempts > 0:
    user_input = int(input("enter the password: "))
    if user_input == password:
        print("access granted")
        break
    else:
        attempts -= 1
        print(f"incorrect password. you have {attempts} attempts left.")    