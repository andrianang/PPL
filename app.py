from menu import Menu
from transaction_manager import TransactionManager

transaction_manager = TransactionManager()
menu = transaction_manager.menu

while True:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "report":
        transaction_manager.report_generate()
    elif user_choice == "off":
        print("Machine turned off.")
        break
    else:
        transaction_manager.process_order(user_choice)
