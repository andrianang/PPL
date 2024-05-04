from coffeemaker import CoffeeMaker
from moneymachine import MoneyMachine
from menu import Menu
from report import Report

class TransactionManager:
    def __init__(self):
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.menu = Menu()
        self.report = Report(self.coffee_maker, self.money_machine)

    def process_order(self, order_name):
        drink = self.menu.find_drink(order_name)
        if drink:
            if self.coffee_maker.is_resource_sufficient(drink):
                if self.money_machine.make_payment(drink.cost):
                    self.coffee_maker.make_coffee(drink)
        else:
            print("Sorry that item is not available.")

    def report_generate(self):
        return self.report.generate_report()
    