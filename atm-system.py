class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

    def authenticate(self, entered_pin):
        return self.pin == entered_pin


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = TransactionHistory()  # Create a TransactionHistory instance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.add_transaction_record(f"Withdrew ${amount}")
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.add_transaction_record(f"Deposited ${amount}")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            self.transaction_history.add_transaction_record(f"Transferred ${amount} to Account {target_account.account_number}")


class ATM:
    def __init__(self):
        self.user = None
        self.active = False

    def start(self):
        self.active = True

    def main_menu(self):
        while self.active:
            print("1. Check Balance")
            print("2. Withdraw Funds")
            print("3. Deposit Funds")
            print("4. Transfer Funds")
            print("5. Transaction History")
            print("6. Quit")
            choice = input("Select an option: ")
            self.process_user_input(choice)

    def get_account_by_number(self, target_account_number):
        accounts = [user1_account, user2_account, user3_account]  # Replace with actual account instances

        for account in accounts:
            if account.account_number == target_account_number:
                return account

        return None

    def process_user_input(self, choice):
        if choice == "1":
            print("Balance:", self.user.account.check_balance())
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if self.user.account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        elif choice == "3":
            amount = float(input("Enter deposit amount: "))
            self.user.account.deposit(amount)
            print("Deposit successful.")
        elif choice == "4":
            target_account_number = input("Enter target account number: ")
            target_account = self.get_account_by_number(target_account_number)  # Use self to access the method
            if target_account:
                amount = float(input("Enter transfer amount: "))
                self.user.account.transfer(target_account, amount)
                print("Transfer successful.")
            else:
                print("Target account not found.")
        elif choice == "5":
            self.user.account.transaction_history.display_transaction_history()  # Access TransactionHistory
        elif choice == "6":
            self.quit()

    def quit(self):
        self.active = False
        print("Thank you for using the ATM. Goodbye!")


class TransactionHistory:
    def __init__(self):
        self.records = []

    def add_transaction_record(self, record):
        self.records.append(record)

    def display_transaction_history(self):
        for record in self.records:
            print(record)


# Example usage:
user1 = User("12345", "1234")
user1_account = Account("0001", 1000.0)
user1.account = user1_account

user2 = User("54321", "4321")
user2_account = Account("0002", 1500.0)
user2.account = user2_account

user3 = User("98765", "5678")
user3_account = Account("0003", 2000.0)
user3.account = user3_account

atm = ATM()
atm.user = user1
atm.start()
atm.main_menu()
