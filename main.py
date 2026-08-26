

import json
from datetime import datetime


def get_valid_date():
    while True:
        date = input("Enter expense date (DD-MM-YYYY): ")

        try:
            valid_date = datetime.strptime(date, "%d-%m-%Y")
            return valid_date.strftime("%d-%m-%Y")

        except ValueError:
            print("Please enter a valid date in DD-MM-YYYY format.")

def get_valid_amount():
    while True:
        amount = input("Enter expense amount: ")

        try:
            amount = float(amount)

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")

def get_valid_category():
    while True:
        category = input("Enter expense category: ")

        category = category.strip()

        if category == "":
            print("Category cannot be empty.")
        else:
            return category.title()

def add_expense():
    amount = get_valid_amount()
    category = get_valid_category()
    date = get_valid_date()

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

def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    print("\nCategory Summary:")

    for category in summary:
        print(category + ":", summary[category])

def search_expenses():
    search_category = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])
            print("--------------------")
            found = True

    if found == False:
        print("No expenses found for this category.")

def search_by_date():
    search_date = get_valid_date()

    found = False

    for expense in expenses:
        if expense["date"] == search_date:
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])
            print("--------------------")
            found = True

    if found == False:
        print("No expenses found for this date.")

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
            save_expenses()
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

            amount = get_valid_amount()
            category = get_valid_category()
            date = get_valid_date()

            expense["amount"] = amount
            expense["category"] = category
            expense["date"] = date
            save_expenses()
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
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Category Summary")
    print("5. Search Expenses")
    print("6. Search by Date")
    print("7. Delete Expense")
    print("8. Edit Expense")
    print("9. Exit")  

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        search_expenses()
    elif choice == "6":
        search_by_date()
    elif choice == "7":
        delete_expense()
    elif choice == "8":
        edit_expense()
    elif choice == "9":        
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")