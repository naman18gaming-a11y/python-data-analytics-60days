#atm menu system
balance = 1000
print("-------welcome to badmash ATM--------")
print("check balance")
print(f"your current balance is: ${balance}")
print("withdraw money")
amount = int(input("enter the amount to withdraw:"))    
total_amount = balance - amount
if total_amount < 0:
    print("insufficient funds")
    deposit_amount = int(input("enter the amount to deposit:"))
    balance += deposit_amount
    print(f"your new balance is: ${balance}")
else:
    balance = total_amount
    print(f"withdrawal successful. your new balance is: ${balance}")    
    exit()