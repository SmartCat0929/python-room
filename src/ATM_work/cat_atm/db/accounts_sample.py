import json

acc_dic = {
    "id": 1234,
    "password": "abc",
    "credit": 15000,
    "balance": 15000,
    "enroll_date": "2019-09-09",
    "exxpire_date": "2022-09-08",
    "pay_day": 22,
    "status": 0  # 0=normal, 1=locked, 2=disabled
}

print(json.dumps(acc_dic))
