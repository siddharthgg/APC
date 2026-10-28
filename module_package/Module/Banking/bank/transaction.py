

def deposit(account, amount):
    if amount > 0:
        account.balance += amount
        print("Amount deposited successfully.")
    else:
        print("Invalid deposit amount.")


def withdraw(account, amount):
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > account.balance:
        print("Insufficient balance.")
    else:
        account.balance -= amount
        print("Amount withdrawn successfully.")