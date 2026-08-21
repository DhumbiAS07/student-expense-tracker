

import json




def add_expense():
    while True:
        amount = input("Enter expense amount: ")

        try:
         amount = float(amount)
         break
        except ValueError:
          print("Please enter a valid number.")

    
    category=input("Enter expense category: ")
    date=input("Enter expense date: ")
    expense = {
       "amount": amount,
       "category": category,
       "date":date
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added!")

def view_expenses():
    print("\nYour Expenses:")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(index, ".")
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])
        print("--------------------")


def calculate_total():
    total = 0

    for expense in expenses:
        total = total + float(expense["amount"])

    print("Total Expenses:", total)

def delete_expense():
    if len(expenses) == 0:
        print("There are no expenses to delete.")
        return

    view_expenses()

    choice = input("Enter the expense number to delete: ")

    try:
        index = int(choice) - 1

        if index >= 0 and index < len(expenses):
            deleted_expense = expenses.pop(index)
            print("Expense deleted:", deleted_expense)
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")

def edit_expense():
    if len(expenses) == 0:
        print("There are no expenses to edit.")
        return

    view_expenses()

    choice = input("Enter the expense number to edit: ")

    try:
        index = int(choice) - 1

        if index >= 0 and index < len(expenses):
            expense = expenses[index]

            print("\nEnter new details:")

            amount = input("Enter new amount: ")
            category = input("Enter new category: ")
            date = input("Enter new date: ")

            expense["amount"] = float(amount)
            expense["category"] = category
            expense["date"] = date

            print("Expense updated!")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

expenses = load_expenses()
while True:
    print("\nStudent Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        edit_expense()
    elif choice == "6":        
       print("Goodbye!")
       break
    else:
        print("Invalid choice. Please try again.")