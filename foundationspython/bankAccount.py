# Build a class with balance, deposit(amount), and withdraw(amount) that refuses to go negative.?


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= 0:
                self.balance -= amount
                print(f"Withdrew: ${amount}. New balance: ${self.balance}.")
            else:
                print("Withdrawal denied. Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")        


account1=BankAccount(100)  # Create a bank account with an initial balance of $100
account1.deposit(50)      # Deposit $50
account1.withdraw(30)     # Withdraw $30







# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")


# account1 = BankAccount(100)

# print("Initial balance:", account1.balance)

# account1.deposit(50)
# print("After deposit:", account1.balance)

# account1.withdraw(40)
# print("After withdrawal:", account1.balance)

# account1.withdraw(200)
# print("Final balance:", account1.balance)

