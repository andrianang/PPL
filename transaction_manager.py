from coffeemaker import CoffeeMaker
from moneymachine import MoneyMachine
from menu import Menu

class TransactionManager:
    def __init__(self):
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.menu = Menu()
        
    def process_order(self, order_name):
        drink = self.menu.find_drink(order_name)
        if drink:
            if self.coffee_maker.is_resource_sufficient(drink):
                if self.money_machine.make_payment(drink.cost):
                    self.coffee_maker.make_coffee(drink)
        else:
            print("Sorry that item is not available.")

    def report_generate(self):
        self.coffee_maker.report()
        self.money_machine.report()
    