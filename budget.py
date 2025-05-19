import math

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
            category.deposit(amount, "Transfer from " + self.name)
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
    
    def _create_spaces(self, description, amount, title):
        spaces = ''
        for _ in range(title - amount - description):
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
        for transaction in self.ledger:
            budget_list += '\n' + transaction['description'][:23:]
            if str(transaction['amount']).find('.') == -1:
                budget_list += self._create_spaces(len(transaction['description'][:23:]), len(str(transaction['amount'])) + 3, len(budget_title)) + str(transaction['amount']) + '.00'
            else:
                budget_list += self._create_spaces(len(transaction['description'][:23:]), len(str(transaction['amount'])), len(budget_title)) + str(transaction['amount'])

        budget_receipt = budget_title + budget_list + f'\nTotal: {str(self.get_balance())}'
        return budget_receipt

def create_spend_chart(categories):
    chart = 'Percentage spent by category'

    category_withdraw = list()
    category_names = list()
    categories_total = 0
    for category in categories:
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                category_withdraw.append(transaction['amount'])
                category_names.append(category.name)
                categories_total -= transaction['amount']
    categories_total = round(categories_total, 2)
    category_withdraw = [math.floor(math.floor((-amount / categories_total) * 100) / 10) * 10 for amount in category_withdraw]
    for percent in range(100, -1, -10):
        chart += f'\n{percent} |'
        for amount in category_withdraw:
            if amount >= percent:
                chart += 'o'
    chart += '\n    '
    for _ in range((len(categories) * 3) + 1):
        chart += '-'
    chart += '\n   '
    for num in range(len(category_names)):
        for category_name in category_names:
            chart += f'  {category_name[num]}'
    return chart

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart({food, clothing}))