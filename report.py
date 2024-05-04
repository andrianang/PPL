class Report:
    def __init__(self, coffee_maker, money_machine):
        self.coffee_maker = coffee_maker
        self.money_machine = money_machine

    def generate_report(self):
        self.coffee_maker.report()
        self.money_machine.report()
