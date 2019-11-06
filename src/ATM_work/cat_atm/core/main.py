import ...

trans_logger = logger.logger("transaction")
access_logger = logger.logger("access")

user_data = {
    "account_id": None,
    "is_authenticated": False,
    "account_data": None
}

def account_info(acc_data):
    print(user_data)