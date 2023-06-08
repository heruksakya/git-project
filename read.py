import json

filename = "finance.json"


def read(txn_id):
    with open(filename, "r") as fp:
        data = json.load(fp)

    user_data = list(filter(lambda x: x['txn_no'] == txn_id, data))
    if user_data:
        print(user_data[0])
    else:
        print("Invalid transaction Number!")
    choice = input("Do you wish to record another transaction? (y/n): ")
    return True if choice == 'y' else False
