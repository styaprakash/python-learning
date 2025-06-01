class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        #add amount to balance
        self.balance += amount #update the balance
        return f"Deposited: {amount}"
    def withdraw(self, amount):
        # subtract if enough balance
        if self.balance < amount:
            return f"The amount can't be withdrawn!"
        self.balance -= amount # update teh balance
        return f"Withdrawn: {amount}"
    def display_balance(self):
        return f"The total balance is: {self.balance}"

# Test
acc1 = BankAccount("Alice", 100)
print(acc1.deposit(50))
print(acc1.withdraw(30))
print(acc1.display_balance())  # Should show 120