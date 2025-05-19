class Category:
    def __init__(self, name):
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
    
    def _create_spaces(self, description_len, amount_len, title_len):
        spaces = ''
        for _ in range(title_len - amount_len - description_len):
            spaces += ' '
        return spaces
    
    def __str__(self):
        budget_title = ''
        for _ in range(int((30 - len(self.name)) / 2)):
            budget_title += '*'
        budget_title += self.name
        for _ in range(30 - len(budget_title)):
            budget_title += '*'
        
        budget_list = ''
        for action in self.ledger:
            budget_list += '\n'  
            for description, amount in action.items():
                budget_list += f'{description}{self._create_spaces(len(description), len(str(amount)), len(budget_title))}{amount}'          
        budget_receipt = budget_title + budget_list
        return budget_receipt


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)