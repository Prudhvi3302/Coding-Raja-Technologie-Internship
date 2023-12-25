import json
from datetime import datetime

class Transaction:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

class Expense(Transaction):
    def __init__(self, category, amount, date):
        super().__init__(category, amount, date)

class Income(Transaction):
    def __init__(self, category, amount, date):
        super().__init__(category, amount, date)

def add_expense(expenses):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    expense = Expense(category, amount, date)
    expenses.append(expense)

def add_income(incomes):
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    income = Income(category, amount, date)
    incomes.append(income)

def calculate_budget(incomes, expenses):
    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    remaining_budget = total_income - total_expense
    return remaining_budget

def save_transactions(file_name, transactions):
    with open(file_name, 'w') as file:
        transactions_data = [vars(transaction) for transaction in transactions]
        json.dump(transactions_data, file)

def load_transactions(file_name):
    try:
        with open(file_name, 'r') as file:
            transactions_data = json.load(file)
            transactions = [Transaction(**data) for data in transactions_data]
            return transactions
    except FileNotFoundError:
        return []

# Example usage
transactions_file = 'transactions.json'
expenses = load_transactions(transactions_file)

# Manual input for expenses
num_expenses = int(input("Enter the number of expenses to add: "))
for _ in range(num_expenses):
    add_expense(expenses)

# Calculate remaining budget
incomes = load_transactions(transactions_file)  # Load incomes (if any)
remaining_budget = calculate_budget(incomes, expenses)
print(f"Remaining Budget: ${remaining_budget}")

# Save transactions
save_transactions(transactions_file, expenses)
