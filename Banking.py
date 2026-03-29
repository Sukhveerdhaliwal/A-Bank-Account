from datetime import datetime
class Transaction:
    def __init__(self, amount, timestamp = None):
        self.amount = float(amount)
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp
    def __repr__(self):
        return f'Transaction({self.amount}, {repr(self.timestamp)})'
    def __str__(self):
        sign = '+' if self.amount > 0 else '-'
        formatted_amount = f'{abs(self.amount): }'
        date_str = self.timestamp.strftime('%Y-%m-%d')
        return f'{date_str}: {sign} ${formatted_amount}'
class Account:
    def __init__(self):
        self.Transactions = []

    def deposit(self, amount):
        amount = abs(float(amount))
        transaction = Transaction(amount)
        self.Transactions.append(transaction)
    def withdraw(self, amount):
        amount = -abs(float(amount))
        transaction = Transaction(amount)
        self.Transactions.append(transaction)
    def get_balance(self):
        return sum(t.amount for t in self.Transactions)