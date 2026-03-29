import datetime as dt
from Banking import Transaction , Account

def test_transaction():
    t = Transaction(100)
    assert t.amount == 100.0
def test_transaction_timestamp_default():
    t = Transaction(100)
    assert isinstance(t.timestamp, dt.datetime)
def test_transaction_timestamp_custom():
    time = dt.datetime(2020, 1, 1)
    t = Transaction(100, time)
    assert t.timestamp == time
def test_transaction_repr():
    time = dt.datetime(2020, 1, 1)
    t = Transaction(50, time)
    assert repr(t) == f"Transaction(50.0, {repr(time)})"
def test_transaction_str_positive():
    time = dt.datetime(2019, 1, 1)
    t = Transaction(1234.56, time)
    assert str(t) == "2019-01-01: + $ 1234.56"
def test_transaction_str_negative():
    time = dt.datetime(2020, 1, 1)
    t = Transaction(-17.25, time)
    assert str(t) == "2020-01-01: - $ 17.25"
def test_deposit_adds_transaction():
    account =Account()
    account.deposit(100)
    assert len(account.Transactions) == 1
    assert  account.Transactions[0].amount == 100
def test_deposit_converts_to_positive():
    account =Account()
    account.deposit(-50)
    assert account.Transactions[0].amount == 50
def test_withdraw_adds_transaction():
    account =Account()
    account.withdraw(40)
    assert account.Transactions[0].amount == -40
def test_withdraw_converts_to_negative():
    account =Account()
    account.withdraw(-10)
    assert account.Transactions[0].amount == -10
def test_balance_no_transaction():
    account = Account()
    assert account.get_balance() == 0
def test_balance_calculation():
    account = Account()
    account.deposit(100)
    account.withdraw(90)
    account.deposit(10)
    assert account.get_balance() == 20

