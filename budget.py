class Category:
    def __init__(self, name, ledger):
        self.name = name
        self.ledger = ledger

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

def create_spend_chart(categories):
    pass