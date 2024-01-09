'''Banking app with a solid UI (user interface)
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
- Checking Account limits
- Confirmation Prompts
'''

import math

def check_bal(current_balance):
    return f"Your current balance is £{current_balance}"

def transfer_funds(current_balance):
    if amount > 0 and amount <= current_balance:
        account_bal = current_balance - amount
        return account_bal
        
    else:
        print("Invalid amount or insufficient funds.")
        return account_bal
def deposit_funds(current_balance):
    if amount >0:
        account_bal = balance + amount
        return account_bal
    
def withdraw_money(current_balance):
    if amount> 0 and amount <= current_balance:
        current_balance -= amount

def check_limits():
    print("Account Limits: ")
    print("- Maximum withdrawal: £500")
    print("- Maximum transfer: £1000")

def confirm_action(action):
    return input("Are you sure you want to {action}? (yes/no):").lower() == "yes"

    
print("Welcome to SafeBank Banking App!\nPlease enter your details below : ")

balance = 150000 #initial balance

while True:
    user_email = input("Enter your email address : ")

    if '@' in user_email and '.' in user_email:
        print("Valid Email")
    else:
        print("Invalid Email, try again!")
        continue

    user_pin = input("Please enter your PIN : ")

    if len(user_pin) == 4 and user_pin.isdigit():
        print("User PIN accepted.")
        break

    else:
        print("Invalid PIN, try again")
#Checking Balances, Transferring Funds, Depositing Money

print("Welcome! Please make a selection below : ")

print("""
1. Check your current balance
2. Transfer funds
3. Deposit money
4. Withdraw money
5. Check account limits
6. Confirmation prompt
""")

choice = input("Please make your selection (enter the number) : ")

if choice == '1':

    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:
        current_balance = check_bal(balance)
        print(current_balance)
    else:
        print("Incorrect PIN")
        

elif choice == '2':
    recipient_email = input("Enter the recipient's email address: ")
    amount = float(input("Please enter the amount you'd like to transfer: "))

    print(f"Successfully transferred £{amount} to {recipient_email}, your account balance is {balance - amount}")

elif choice == "3":
    confirm_pin = input("Please enter your pin to confirm action: ")
    amount = float(input("Please enter the deposit amount: "))

    if user_pin == confirm_pin:
        deposit_funds(balance)
        print("deposit_amount")
    else:
        print("Incorrect pin ")

    print(f"Deposit successful! You have deposited £{amount}, your total balance is {amount + balance}")

    
elif choice == "4":
    confirm_pin = input("Please enter your pin to confirm action: ")
    amount = float(input("Please enter the amount you'd like to withdraw: "))
    if user_pin == confirm_pin:
        withdraw_money(balance) 
    else:
        print("Invalid withdrawal")

    print(f"The total amount of {amount} successfully withdrawn!, your balance is {balance-amount}")


elif choice == "5":
    check_limits()

elif choice == "6":
    action = input("Are you sure you want to {action}? (yes/no):").lower() == "yes" 

else: 
    
    print("Invalid selection. Please enter a valid number")


