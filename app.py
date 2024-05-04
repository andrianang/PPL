from menu import Menu
from transaction_manager import TransactionManager

menu = Menu()
transaction_manager = TransactionManager()

while True:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()
    if user_choice == "report":
        transaction_manager.report()
    elif user_choice == "off":
        print("Machine turned off.")
        break
    else:
        transaction_manager.process_order(user_choice)
