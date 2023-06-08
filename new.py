import json
import os
filename = "finance.json"


def new():
    txn_type = input("Enter the type of transaction (i for income/e for expense): ")
    if txn_type == 'i':
        txn_type = "Income"
    elif txn_type == 'e':
        txn_type = "Expense"
    else:
        print("Invalid type of transaction!")
        choice = input("Do you wish to record another transaction? (y/n): ")
        return True if choice == 'y' else False
    txn_no = input("Enter your transaction number: ")
    entry = float(input("Enter the amount: "))
    entry_type = input("Enter the status of transaction: ")
    if txn_type == 'Income' and entry_type == 'r':
        entry_type = "Received"
    elif txn_type == 'Income' and entry_type == 'p':
        entry_type = "Pending"
    elif txn_type == 'Expense' and entry_type == 'c':
        entry_type = "Cleared"
    elif txn_type == 'Expense' and entry_type == 'p':
        entry_type = "Pending"
    else:
        print("Invalid input!")
    user_data = dict(txn_no=txn_no, entry_type=entry_type, entry=entry,  txn_type=txn_type)
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
    print(f"TRANSACTION SUCCESSFUL!\nYOUR TRANSACTION DETAILS:\nTransaction type: {txn_type}\n"
          f"Amount: {entry}. Status: {entry_type}.")
    choice = input("Do you wish to record another transaction? (y/n): ")
    return True if choice == 'y' else False
