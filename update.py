import json
filename = "finance.json"


def update(txn_id, to_update, changed_info):
    with open(filename, "r+") as fp:
        data = json.load(fp)
        for user_data in data:
            if user_data['txn_no'] == txn_id:
                user_data[to_update] = changed_info
                break
        fp.seek(0)
        fp.write(json.dumps(data, indent=2))
    print("Transaction information updated successfully!")
    choice = input("Do you wish to record another transaction? (y/n): ")
    return True if choice == 'y' else False
