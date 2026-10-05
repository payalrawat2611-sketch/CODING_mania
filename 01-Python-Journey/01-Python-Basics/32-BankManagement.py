# miniproject 2 
class BankAccount:

    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    def show_details(self):
        print("\n----- Account Details -----")
        print(f"Name       : {self.name}")
        print(f"Account No : {self.account_no}")
        print(f"Balance    : ₹{self.__balance}")


def main():

    print("----- BANK ACCOUNT MANAGER ------")

    name = input("Enter your name: ")
    account_no = input("Enter account number: ")

    account = BankAccount(name, account_no)

    while True:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = float(input("Enter amount: "))
                account.deposit(amount)

            elif choice == 2:
                amount = float(input("Enter amount: "))
                account.withdraw(amount)

            elif choice == 3:
                account.check_balance()

            elif choice == 4:
                account.show_details()

            elif choice == 5:
                print("Thank you for using our bank.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


main()