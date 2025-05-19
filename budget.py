class Category:
    def __init__(self, name, ledger):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount' : -amount, 'description' : description})
            return True
        return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            self.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    
    def get_balance(self):
        total = 0
        for process in self.ledger:
            for key, value in process.items():
                if key == 'amount':
                    total += value
        return total
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
    def __str__(self):
        title = ''
        for _ in range((30 - len(self.name)) / 2):
            title += '*'
        title += self.name
        for _ in range(30 - len(title)):
            title += '*'