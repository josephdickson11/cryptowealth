account_balance = 670
account_name = "Rani"
account_type = "savings"
indebt = False


import datetime
import xdrlib

x = datetime.datetime(2018, 9, 15)


# print(datetime.date.today())

yesterday = datetime.datetime(2022, 1, 13)
# print(yesterday)

today = datetime.date.today()
# print(today)


def credit_account():
    account_balance = 670
    account_name = "Rani"
    account_type = "savings"
    indebt = False
    is_verified = False
    account_limit = 5000

    print("current account balance is : ", account_balance)
    amount_to_credit = int(input("please enter amount to credit: "))

    if amount_to_credit > account_limit:
        if is_verified:
            account_balance = account_balance + amount_to_credit
            print("credit successful, your new account balance is", account_balance)
        else:
            print("kindly verify account and try again")
    else:
        account_balance = account_balance + amount_to_credit
        print("credit successful, your new account balance is", account_balance)

    return account_balance
