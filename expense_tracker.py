import datetime
import json
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ['food', 'transportation', 'entertainment', 'utilities', 'others']
        self.load_data()

    def load_data(self):
        if os.path.exists('expenses.json'):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)

    def save_data(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, description, category):
        if category not in self.categories:
            print(f"Invalid category. Choose from {self.categories}")
            return
        self.expenses.append({
            'amount': amount, 'description': description, 'category': category,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_data()
        print("Expense added successfully.")

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Amount: {expense['amount']}, Description: {expense['description']}, "
                  f"Category: {expense['category']}, Date: {expense['date']}")

    def view_summary(self):
        monthly_summary = {}
        category_summary = {category: 0 for category in self.categories}
        for expense in self.expenses:
            month = expense['date'][:7]
            monthly_summary[month] = monthly_summary.get(month, 0) + expense['amount']
            category_summary[expense['category']] += expense['amount']
        print("Monthly Summary:")
        for month, total in monthly_summary.items():
            print(f"{month}: {total}")
        print("\nCategory Summary:")
        for category, total in category_summary.items():
            print(f"{category}: {total}")

def main():
    tracker = ExpenseTracker()
    menu = "\nExpense Tracker Menu:\n1. Add Expense\n2. View Expenses\n3. View Summary\n4. Exit\n"
    actions = {'1': tracker.add_expense, '2': tracker.view_expenses, '3': tracker.view_summary}

    while True:
        choice = input(menu + "Enter your choice: ")
        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input(f"Enter category ({', '.join(tracker.categories)}): ")
                tracker.add_expense(amount, description, category)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice in actions:
            actions[choice]()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
