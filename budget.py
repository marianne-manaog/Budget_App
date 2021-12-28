# This Python file contains a 'Budget' class that can be used to instantiate objects
# based on different budget categories, such as food, clothing, and entertainment.
# These objects allow for depositing and withdrawing funds from each category,
# as well computing category balances.


from typing import List

# TODO: Add class' and methods' docstrings
# TODO: Implement method to transfer balance amounts between categories.
# TODO: Add unit tests for class' methods


class Budget:

    def __init__(self, balance: float, category: str, ledger: List):
        self.balance = balance
        self.category = category
        self.ledger = ledger

    def __repr__(self):
        return f"The budget for {self.category} has £{self.balance} remaining."
            
    def deposit(self, deposit_amount: float, description: str):
        self.balance += deposit_amount
        self.ledger.append({"amount": deposit_amount, "description": description})
        return self.balance, self.category

    def withdraw(self, withdraw_amount: float, description: str):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            self.ledger.append({"amount": withdraw_amount, "description": description})
        else:
            raise Exception(f"Insufficient amount to withdraw.")
        return self.balance, self.category
