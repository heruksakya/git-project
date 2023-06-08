from expense import expense
from income import income
from read import read
from delete import delete
from update import update


def inquiry():
    selection = input("i for Income\ne for Expense\nr for Read\nd for delete\nu for update\nEnter your choice: ")
    selection = selection.lower()

    def exit_msg():
        print("Thank you for using Money tracker!")

    if selection == 'i':
        contd = income()
        inquiry() if contd else exit_msg()

    elif selection == 'e':
        contd = expense()
        inquiry() if contd else exit_msg()

    elif selection == 'r':
        txn_no = input("Enter the Transaction Number: ")
        contd = read(txn_no)
        inquiry() if contd else exit_msg()

    elif selection == 'd':
        choice = input("Delete all transaction? (y/n): ")
        if choice.lower() == 'y':
            contd = delete('y')
        else:
            txn_no = input("Enter transaction number: ")
            contd = delete(txn_no)
        inquiry() if contd else exit_msg()

    elif selection == 'u':
        txn_no = input("Enter the transaction number: ")
        to_update = input("Enter the information you want to update (txn_no/entry): ")
        if to_update.lower() not in ["txn_no", "entry"]:
            print("Invalid transaction number!")
            exit_msg()
        else:
            changed_info = input(f"Enter new {to_update}: ")
            contd = update(txn_no, to_update, changed_info)
            inquiry() if contd else exit_msg()
    else:
        print("Invalid input!")


if __name__ == "__main__":
    inquiry()
