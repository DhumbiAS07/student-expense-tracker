expenses = []

def add_expense():
    amount=input("Enter expense amount: ")
    category=input("Enter expense category: ")

    expense = {
       "Amount": amount,
       "Category": category
    }
    expenses.append(expense)

    print("Expense added!")

def view_expenses():
    print("\nYour Expenses:")

    for expense in expenses:
        print("Amount:", expense["Amount"])
        print("Category:", expense["Category"])
        print("--------------------")


def calculate_total():
    total = 0

    for expense in expenses:
        total = total + float(expense["Amount"])

    print("Total Expenses:", total)


while True:
    print("\nStudent Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
         print("Goodbye!")
         break
    else:
        print("Invalid choice. Please try again.")