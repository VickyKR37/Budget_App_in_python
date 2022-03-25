# “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, 
# and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing 
# category balances and transferring balance amounts between categories”

class Budget():
    def __init__(self, amount, categories):
        self.amount = amount
        self.categories = categories
    
    
    def __repr__(self):
        return f"{self.amount}"

    def withdraw(self, withdrawal_amount):
        self.amount -= withdrawal_amount
        return withdrawal_amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount
        return deposit_amount

   


