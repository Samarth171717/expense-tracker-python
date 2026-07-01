from datetime import datetime
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()
    def load_expenses(self):
        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    self.expenses.append({
                        "date": parts[0],
                        "category": parts[1],
                        "amount": int(parts[2])
                    })
        except FileNotFoundError:
            pass

    def add_expense(self):
        print("\n===== Add Expense =====\n")
        category = input("Enter the category")
        amount = int(input("Enter the amount"))
        date = datetime.now().strftime("%m/%d/%Y")
        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }
        self.expenses.append(expense)
        with open('expenses.txt', 'a') as file:
            file.write(f"{date},{category},{amount}\n")
        print("\nExpense added successfully\n")

    def view_expenses(self):
        print("\n===== View Expense =====\n")
        if len(self.expenses) == 0:
            print("No expense found")
        else:
            for index,expense in enumerate(self.expenses,start=1):
                print(
                    f"{index}\t"
                    f"date:{expense['date']} - category: {expense['category']} - amount: ₹{expense['amount']}"
                )

    def total_expenses(self):
        print("\n===== Total Expense =====")
        total = 0
        for expense in self.expenses:
            total += expense['amount']
        print(f"Total Expense:₹{total}\n")

    def delete_expense(self):
        print("\n===== Delete Expense =====")
        if len(self.expenses)==0:
            print("No expense found\n")
        else:
            try:
                n=int(input("Enter the index to be deleted:"))
                self.expenses.pop(n-1)
                with open('expenses.txt', 'w') as file:
                    for expense in self.expenses:
                        file.write(f"{expense['date']},{expense['category']},{expense['amount']}\n")
                print("\nExpense deleted successfully\n")
            except ValueError:
                print("\nPlease enter a number\n")
            except IndexError:
                print("\nInvalid index\n")

    def search_expense(self):
        print("\n===== Search Expense =====")
        search_category = input("Enter the category to be searched:").lower()
        found = False
        for expense in self.expenses:
            if expense['category'].lower() == search_category:
                found = True
                print(f"{expense['date']},{expense['category']},{expense['amount']}")
        if not found:
            print("\nNo Category found\n")

tracker = ExpenseTracker()
while True:
    print(
    "\n===== Expense Tracker =====\n"
    "1. Add Expense\n"
    "2. View Expense\n"
    "3. Total Expense\n"
    "4.Delete Expense\n"
    "5.Search Expense\n"
    "6. Exit\n"
    )
    try:
        choice = int(input("Enter the choice"))
        if choice==1:
            tracker.add_expense()
        elif choice==2:
            tracker.view_expenses()
        elif choice==3:
            tracker.total_expenses()
        elif choice==4:
            tracker.delete_expense()
        elif choice==5:
            tracker.search_expense()
        elif choice==6:
            print("\nGoodbye 👋\n")
            break
        else:
            print("\nInvalid choice.Please try again\n")
    except ValueError:
        print("\nPlease enter a valid number\n")
