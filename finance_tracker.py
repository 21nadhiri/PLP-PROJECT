import json
from datetime import datetime, timedelta

from collections import defaultdict

# File to store transactions and budgets
TRANSACTIONS_FILE = "transactions.json"
BUDGETS_FILE = "budgets.json"

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def add_transaction(transactions, type, amount, category, description):
    transaction = {
        "type": type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    transactions.append(transaction)
    save_data(transactions, TRANSACTIONS_FILE)

def calculate_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    return income - expenses

def filter_transactions_by_date(transactions, start_date, end_date):
    return [t for t in transactions if start_date <= datetime.strptime(t["date"], "%Y-%m-%d %H:%M:%S") <= end_date]

def generate_report(transactions, start_date=None, end_date=None):
    if start_date and end_date:
        filtered_transactions = filter_transactions_by_date(transactions, start_date, end_date)
    else:
        filtered_transactions = transactions

    balance = calculate_balance(filtered_transactions)
    income = sum(t["amount"] for t in filtered_transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in filtered_transactions if t["type"] == "expense")
    
    print("\n--- Financial Report ---")
    if start_date and end_date:
        print(f"Date Range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}")
    
    categories = defaultdict(float)
    for t in filtered_transactions:
        if t["type"] == "expense":
            categories[t["category"]] += t["amount"]
    
    print("\nExpense Breakdown by Category:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")


def set_budget(budgets, category, amount):
    budgets[category] = amount
    save_data(budgets, BUDGETS_FILE)

def check_budget_status(transactions, budgets):
    current_month = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    next_month = (current_month + timedelta(days=32)).replace(day=1)
    
    monthly_expenses = defaultdict(float)
    for t in filter_transactions_by_date(transactions, current_month, next_month):
        if t["type"] == "expense":
            monthly_expenses[t["category"]] += t["amount"]
    
    print("\n--- Budget Status ---")
    for category, budget in budgets.items():
        spent = monthly_expenses.get(category, 0)
        remaining = budget - spent
        print(f"{category}: ")
        print(f"  Budget: ${budget:.2f}")
        print(f"  Spent: ${spent:.2f}")
        print(f"  Remaining: ${remaining:.2f}")
        print(f"  Status: {'Over budget' if remaining < 0 else 'Within budget'}")

def main():
    print("Welcome to the Personal Finance Tracker!")
    
    transactions = load_data(TRANSACTIONS_FILE)
    budgets = load_data(BUDGETS_FILE)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Visualize Expenses")
        print("5. Visualize Income vs Expenses")
        print("6. Set Budget")
        print("7. Check Budget Status")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            amount = float(input("Enter income amount: $"))
            category = input("Enter income category: ")
            description = input("Enter description: ")
            add_transaction(transactions, "income", amount, category, description)
            print("Income added successfully!")
        
        elif choice == "2":
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            add_transaction(transactions, "expense", amount, category, description)
            print("Expense added successfully!")
        
        elif choice == "3":
            use_date_range = input("Do you want to filter by date range? (y/n): ").lower() == 'y'
            if use_date_range:
                start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
                end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
                generate_report(transactions, start_date, end_date)
            else:
                generate_report(transactions)
        
       
        
        elif choice == "6":
            category = input("Enter budget category: ")
            amount = float(input("Enter budget amount: $"))
            set_budget(budgets, category, amount)
            print("Budget set successfully!")
        
        elif choice == "7":
            check_budget_status(transactions, budgets)
        
        elif choice == "8":
            print("Thank you for using the Personal Finance Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
