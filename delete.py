import json
filename = "finance.json"


def delete(txn_id):
    with open(filename, "r+") as fp:
        data = json.load(fp)
        if txn_id == 'y':
            data.clear()
            print("All transactions deleted successfully!")
        else:
            for user_data in data:
                if user_data['txn_no'] == txn_id:
                    print("Transaction deleted successfully!")
                    data.remove(user_data)
                    break
            else:
                print("Invalid Transaction Number!")

        fp.seek(0)
        fp.truncate()
        json.dump(data, fp, indent=2)

    choice = input("Do you wish to record another transaction? (y/n): ")
    return True if choice == 'y' else False
