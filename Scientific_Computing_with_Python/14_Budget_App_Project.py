class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.budget = 0
    
    def __str__(self):
        result = self.category.center(30, "*") + '\n'
        for item in self.ledger:
            description = str(item['description']).ljust(23)[:23]
            amount = f"{item['amount']:.2f}".rjust(7)
            result += f"{description}{amount}\n"
        result += f"Total: {self.budget}"
        return result

    def deposit (self, amount, description = ''):
        self.description = description
        if amount > 0:
            self.amount = amount
            self.budget += self.amount
            self.ledger.append({'amount': self.amount, 'description': self.description})

    def check_funds(self, amount):
        if amount <= self.budget:
            return True
        return False

    def withdraw (self, amount, description = ''):
        self.description = description
        if self.check_funds(amount):
            self.amount = -amount      
            self.budget += self.amount
            self.ledger.append({'amount': self.amount, 'description': self.description})
            return True
        print("Not enough funds!")
        return False

    def get_balance(self):        
        return self.budget

    def transfer(self, amount, to_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {to_category.category}")
            to_category.deposit(amount, f"Transfer from {self.category}" )
            return True
        return False

def create_spend_chart(categories):

    spend_by_category = []
    category_summary = 0
    total_withdraw = 0

    for category in categories:
        for item in category.ledger:
            if item['amount'] < 0 and item['description'][0:8] != 'Transfer':
                category_summary += -item['amount'] 
                total_withdraw += -item['amount']
    
        spend_by_category.append({'category': category.category,'amount': category_summary})
        category_summary = 0

    for item in spend_by_category:
        item['percentage'] = (item['amount'] / total_withdraw * 100) // 10 * 10
    chart = "Percentage spent by category\n"

    for i in range (100, -1, -10):
        chart += f"{str(i).rjust(3)}| " + "  ".join("o" if i <= item["percentage"]\
        else " " for item in spend_by_category) + "  \n"

    chart += ' ' * 4 + "-" * (len(spend_by_category) * 3 + 1) + "\n"
    max_lenght = max(len(item['category']) for item in spend_by_category)

    for letter in zip(*(item['category'].ljust(max_lenght)\
    for item in spend_by_category)):
        chart += " " * 5 + "  ".join(letter) + "  \n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.deposit(100, 'deposit')
clothing.withdraw(15.20, 'panties')
food.transfer(50, clothing)

categories = [food, clothing]
print(create_spend_chart(categories))