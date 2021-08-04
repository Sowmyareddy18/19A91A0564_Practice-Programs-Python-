class MyException(Exception):
    pass
try:
    balance=10000
    amount=float(input("enter amount to be withdrawn"))
    if balance<amount:
        raise MyException
    balance-=amount
    print("Balance is",balance)
except MyException:
    print("Balance is insufficient")
