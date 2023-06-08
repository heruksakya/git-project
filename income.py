import json
import os
filename = "finance.json"


def income():
    txn_no = input("Enter your transaction number: ")
    entry = float(input("Enter the amount: "))
    entry_type = input("Enter the type of income (r for received, p for pending): ")
    txn_type = "Income"
    user_data = dict(txn_no=txn_no, entry=entry, entry_type=entry_type, txn_type=txn_type)

    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            json_obj = json.dumps([user_data], indent=2)
            fp.write(json_obj)
    else:
        with open(filename, "r+") as fp:
            data = fp.read()
            data = json.loads(data)
            data.append(user_data)
            fp.seek(0)
            fp.write(json.dumps(data, indent=2))
    if entry_type == 'r':
        income_type = "Received"
    elif entry_type == 'p':
        income_type = "Pending"
    else:
        print("Invalid input!")
        exit_choice = input("Do you want to continue? (y/n): ")
        return True if exit_choice == 'y' else False
    print(f"TRANSACTION SUCCESSFUL!\nYOUR TRANSACTION DETAILS:\nTransaction type: Income\nAmount: {entry}. Status: {income_type}.")
    choice = input("Do you wish to record another transaction? (y/n): ")
    return True if choice == 'y' else False
