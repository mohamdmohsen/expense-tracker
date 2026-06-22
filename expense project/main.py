from database import init_db, add_expense, view_expenses ,delete_expense
init_db()
def show_menu():
    print("Welcome to Expense Tracker")
    print('1. Add Expense')
    print('2. View Expenses')
    print("3. Delete Expense")
    print("4. Exit")




def main():
 while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == '1':
     name = input("Enter item name: ")
     try:
      price = float(input("Enter price: "))
     except ValueError:
      print("Invalid price. Please enter a number.")
      continue
     category = input("Enter category: ")
     add_expense(name,price,category)
     print("Expense added")

    elif choice == '2':
     for row in view_expenses():
      print(row)
    elif choice == '3': 
        try:
            id = int(input("Enter expense ID to delete: "))
            delete_expense(id)
            print("Expense deleted")
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")

    elif choice == '4': 
        break
    else: 
        print("Invalid input please try again")

main()        