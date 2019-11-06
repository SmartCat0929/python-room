def acc_auth(account,password):
    db_path = db_handler.db_handler(settings,DATABASE)
    account_file="%s/%s.json"%(db_path,account)
    print(account_file)
    if os.path.isfile(account_file)
        with open(account_file):
