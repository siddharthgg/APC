

from bank.account import Account
from bank.transaction import deposit, withdraw
from bank.loan import calculate_loan

# Account creation
name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))

account = Account(name, account_number, initial_balance)

print("\n----- Account Details -----")
account.display_account()

# Deposit
amount = float(input("\nEnter amount to deposit: "))
deposit(account, amount)
print("Current Balance:", account.balance)

# Withdrawal
amount = float(input("\nEnter amount to withdraw: "))
withdraw(account, amount)
print("Current Balance:", account.balance)

# Loan calculation
principal = float(input("\nEnter loan amount: "))
rate = float(input("Enter interest rate (%): "))
years = int(input("Enter loan period (years): "))

interest, total = calculate_loan(principal, rate, years)

print("\n----- Loan Details -----")
print("Loan Amount:", principal)
print("Interest:", interest)
print("Total Repayment Amount:", total)