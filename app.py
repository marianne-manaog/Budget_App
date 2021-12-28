# This Python file runs 'budget.py' for budgeting purposes (deposit and/or withdrawal)
# across various categories.
import logging

from budget import Budget


logging.getLogger().setLevel(logging.INFO)

# Define 'Budget' class' inputs to instantiate objects
balance = float(input("Enter balance: "))
category = input("Enter category: ")
# Assume ledger is empty, as there are no transactions yet
ledger = []

# Object based on a specific category ('Food', 'Clothing', or 'Entertainment')
budget_object = Budget(balance, category, ledger)

logging.info(budget_object)

# Transactions for deposit
number_of_transactions_for_deposit = int(input("Enter number of transactions for deposit: "))

for i in range(number_of_transactions_for_deposit):
    deposit_amount = float(input("Enter amount to deposit: "))
    deposit_description = input("Enter description of amount to deposit: ")
    budget_object.deposit(deposit_amount, deposit_description)
    logging.info(f"You deposited the amount of £{deposit_amount} for the category {budget_object.category}")
    logging.info(f"The transaction is for {budget_object.ledger}")
    logging.info(f"Your current balance is £{budget_object.balance}.")

# Transactions for withdrawal
number_of_transactions_for_withdrawal = int(input("Enter number of transactions for withdrawal: "))

for i in range(number_of_transactions_for_withdrawal):
    withdrawal_amount = float(input("Enter amount to withdraw: "))
    withdrawal_description = input("Enter description of amount to withdraw: ")
    budget_object.withdraw(withdrawal_amount, withdrawal_description)
    logging.info(f"You withdrew the amount of £{withdrawal_amount} for the category {budget_object.category}")
    logging.info(f"The transaction is for {budget_object.ledger}")
    logging.info(f"Your current balance is £{budget_object.balance}.")
