from unicodedata import category
from datetime import datetime
expenses=[]
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            parts=line.strip().split(",")
            expenses.append({
                "date": parts[0],
                "category": parts[1],
                "amount": int(parts[2])
            })
except FileNotFoundError:
    print("No expenses file found")

while True:
    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4.Delete Expense")
    print("5.Search Expense")
    print("6. Exit")

    choice=int(input("Enter the choice"))
    if choice==1:
      print("Add Expense selected")
      category=input("Enter the category")
      amount=int(input("Enter the amount"))
      date=datetime.now().strftime("%m/%d/%Y")
      expense = {
          "date": date,
          "category": category,
          "amount": amount
      }
      expenses.append(expense)
      with open('expenses.txt', 'a') as file:
          file.write(f"{date},{category},{amount}\n")
      print("Expense added successfully")

    elif choice==2:
        print("View Expense selected")
        if len(expenses) == 0:
            print("No expense found")
        else:
            for index,expense in enumerate(expenses,start=1):
                print(
                    f"{index}\t"
                    f"date:{expense['date']} - category: {expense['category']} - amount: ₹{expense['amount']}"
                )
    elif choice==3:
        print("Total Expense selected")
        total=0
        for expense in expenses:
            total+=expense['amount']
        print("Total Expense: ", total)
    elif choice==4:
        if len(expenses)==0:
            print("No expense found")
        else:
            try:
                n=int(input("Enter the index to be deleted:"))
                expenses.pop(n-1)
                with open('expenses.txt', 'w') as file:
                    for expense in expenses:
                        file.write(f"{expense['date']},{expense['category']},{expense['amount']}\n")
                print("Expense deleted successfully")
            except ValueError:
                print("Please enter a number")
            except IndexError:
                print("Invalid index")
    elif choice==5:
        search_category=input("Enter the category to be searched:").lower()
        found=False
        for expense in expenses:
            if expense['category'].lower() == search_category:
                found=True
                print(f"{expense['date']},{expense['category']},{expense['amount']}")
        if not found:
            print("No Category found")
    elif choice==6:
        print("Goodbye")
        break
    else:
        print("Invalid Choice.Please give a valid choice")
