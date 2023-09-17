import tkinter as tk
from tkinter import messagebox

# Define a dictionary to store account numbers, PINs, usernames, and balances (for demonstration purposes)
# You should replace this with a secure authentication mechanism (e.g., database)
account_data = {
    "123456": {"pin": "1234", "username": "User1", "balance": 1000.0},
    "789012": {"pin": "5678", "username": "User2", "balance": 1500.0},
}

# Initialize a dictionary to store transfer history for each account
transfer_history = {}

class ATM:
    def __init__(self):
        self.account_number = None  # Store the authenticated account number
        self.balance = 0
        self.create_login_window()

    def create_login_window(self):
        self.login_window = tk.Tk()
        self.login_window.title("Login")
        self.login_window.configure(bg='#2a1b3d')

        login_label = tk.Label(self.login_window, text="Enter Account Number and PIN", font=("Helvetica", 16, "bold"), bg='#2a1b3d', fg='white')
        login_label.pack(pady=10)

        self.account_number_entry = tk.Entry(self.login_window, bg='#a4b3b6', fg='black', borderwidth=5)
        self.account_number_entry.pack(pady=5, padx=20)

        self.pin_entry = tk.Entry(self.login_window, bg='#a4b3b6', fg='black', borderwidth=5, show="*")
        self.pin_entry.pack(pady=5, padx=20)

        login_button = tk.Button(self.login_window, text="Login", relief='raised', command=self.authenticate, padx=20, bg='#1f2833', fg='white')
        login_button.pack(pady=10)

    def authenticate(self):
        account_number = self.account_number_entry.get()
        pin = self.pin_entry.get()

        # Check if the account number and PIN are valid
        if account_number in account_data and account_data[account_number]["pin"] == pin:
            self.account_number = account_number  # Store the authenticated account number
            self.login_window.destroy()
            self.create_main_window()
        else:
            messagebox.showerror("Authentication Failed", "Invalid account information. Please try again.")

    def create_main_window(self):
        self.main_window = tk.Tk()
        self.main_window.title("ATM Machine")
        self.main_window.configure(bg='white')

        bank_name_label = tk.Label(self.main_window, text="Bank of Students", font=("Helvetica", 30, "bold"), bg='white', fg='#44318d')
        bank_name_label.pack(pady=10)

        self.create_transaction_ui()

    def create_transaction_ui(self):
        def show_account_detail():
            self.account_detail()

        def show_balance():
            self.check_balance()

        def deposit_funds():
            amount_str = deposit_amount_entry.get()
            try:
                amount = float(amount_str)
                self.deposit(amount)
            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid amount.")

        def withdraw_funds():
            amount_str = withdraw_amount_entry.get()
            try:
                amount = float(amount_str)
                self.withdraw(amount)
            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid amount.")

        def show_transfer_history():
            self.view_transfer_history()

        def open_transfer_window():
            self.create_transfer_window()

        # Create a frame to group widgets
        frame = tk.Frame(self.main_window, bg='#1f2833', padx=10, pady=10)
        frame.pack()

        # Create a sub-frame for account details
        account_frame = tk.Frame(frame, bg='#1f2833')
        account_frame.pack(pady=10)

        name_label = tk.Label(account_frame, text=f"Account Number: {self.account_number}", font=("Helvetica", 12), bg='#1f2833', fg='white')
        name_label.pack()

        account_detail_button = tk.Button(account_frame, text="Account Details", relief='raised', command=show_account_detail, padx=20, bg='#1f2833', fg='white')
        account_detail_button.pack(side='left', padx=10)

        view_history_button = tk.Button(account_frame, text="View Transaction History", relief='raised', command=show_transfer_history, padx=20, bg='#1f2833', fg='white')
        view_history_button.pack(side='left', padx=10)

        check_balance_button = tk.Button(account_frame, text="Check Balance", relief='raised', command=show_balance, padx=20, bg='#1f2833', fg='white')
        check_balance_button.pack(side='left', padx=10)

        # Create a frame for transaction-related widgets
        transaction_frame = tk.Frame(frame, bg='#1f2833')
        transaction_frame.pack(padx=10, pady=10)

        deposit_label = tk.Label(transaction_frame, text="Enter deposit amount (₹.):", bg='#1f2833', fg='green')
        deposit_label.pack()
        deposit_amount_entry = tk.Entry(transaction_frame, bg='#a4b3b6', fg='black', borderwidth=5)
        deposit_amount_entry.pack()

        deposit_button = tk.Button(transaction_frame, text="Deposit", relief='raised', command=deposit_funds, bg='green', fg='white')
        deposit_button.pack(pady=10)

        withdraw_label = tk.Label(transaction_frame, text="Enter withdrawal amount (₹.):", bg='#1f2833', fg='red')
        withdraw_label.pack()
        withdraw_amount_entry = tk.Entry(transaction_frame, bg='#a4b3b6', fg='black', borderwidth=5, width=20)
        withdraw_amount_entry.pack()

        withdraw_button = tk.Button(transaction_frame, text="Withdraw", relief='raised', command=withdraw_funds, bg='red', fg='white')
        withdraw_button.pack(pady=10, padx=10)

        # Create a frame for current balance
        balance_frame = tk.Frame(frame, bg='#1f2833')
        balance_frame.pack(pady=20)

        balance_label = tk.Label(balance_frame, text="Current Balance:", font=("Helvetica", 12), bg='#1f2833', fg='white')
        balance_label.pack()

        self.balance_value_label = tk.Label(balance_frame, text=f"₹.{account_data[self.account_number]['balance']:.2f}", font=("Helvetica", 12), bg='#1f2833', fg='white')
        self.balance_value_label.pack()

        

        transfer_button = tk.Button(frame, text="Transfer", relief='raised', command=open_transfer_window, bg='#1f2833', fg='white')
        transfer_button.pack( padx=10)
        
        # Create a frame for exit button
        exit_frame = tk.Frame(frame, bg='#1f2833')
        exit_frame.pack()

        exit_button = tk.Button(exit_frame, text="Exit", relief='raised', command=self.main_window.destroy, bg='#1f2833', fg='white')
        exit_button.pack(pady=10)

    def account_detail(self):
        # Retrieve account details from the account_data dictionary
        username = account_data[self.account_number]["username"]
        balance = account_data[self.account_number]["balance"]

        messagebox.showinfo("Account Detail", f"Account Number: {self.account_number}\nUsername: {username}\nAvailable Balance: ₹.{balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            # Update the balance in the account_data dictionary
            account_data[self.account_number]["balance"] += amount
            self.update_balance_label()

            # Record the deposit in transfer history
            if self.account_number not in transfer_history:
                transfer_history[self.account_number] = []
            transfer_history[self.account_number].append(f"Deposited ₹.{amount:.2f}")

            messagebox.showinfo("Deposit", f"₹.{amount:.2f} deposited successfully!\nCurrent Balance: ₹.{account_data[self.account_number]['balance']:.2f}")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid deposit amount.")

    def create_transfer_window(self):
        self.transfer_window = tk.Tk()
        self.transfer_window.title("Transfer Funds")
        self.transfer_window.configure(bg='#2a1b3d')

        transfer_label = tk.Label(self.transfer_window, text="Transfer Funds", font=("Helvetica", 16, "bold"), bg='#2a1b3d', fg='white')
        transfer_label.pack(pady=10)

        recipient_label = tk.Label(self.transfer_window, text="Recipient's Account Number:", bg='#2a1b3d', fg='white')
        recipient_label.pack()
        recipient_entry = tk.Entry(self.transfer_window, bg='#a4b3b6', fg='black', borderwidth=5)
        recipient_entry.pack()

        amount_label = tk.Label(self.transfer_window, text="Enter transfer amount (₹.):", bg='#2a1b3d', fg='white')
        amount_label.pack()
        amount_entry = tk.Entry(self.transfer_window, bg='#a4b3b6', fg='black', borderwidth=5)
        amount_entry.pack()

        transfer_button = tk.Button(self.transfer_window, text="Transfer", relief='raised', command=lambda: self.transfer_funds(recipient_entry.get(), amount_entry.get()), bg='#1f2833', fg='white')
        transfer_button.pack(pady=10)

    def transfer_funds(self, to_account, amount_str):
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid amount.")
            return

        if amount > 0:
            if to_account in account_data:
                if amount <= account_data[self.account_number]["balance"]:
                    # Update the balance in the sender's account_data
                    account_data[self.account_number]["balance"] -= amount
                    self.update_balance_label()

                    # Update the balance in the recipient's account_data
                    account_data[to_account]["balance"] += amount

                    # Record the transfer in transfer history for both accounts
                    if self.account_number not in transfer_history:
                        transfer_history[self.account_number] = []
                    if to_account not in transfer_history:
                        transfer_history[to_account] = []

                    transfer_history[self.account_number].append(f"Transferred ₹.{amount:.2f} to {to_account}")
                    transfer_history[to_account].append(f"Received ₹.{amount:.2f} from {self.account_number}")

                    messagebox.showinfo("Transfer", f"₹.{amount:.2f} transferred to {to_account} successfully!\nCurrent Balance: ₹.{account_data[self.account_number]['balance']:.2f}")
                else:
                    messagebox.showerror("Insufficient Funds", f"Insufficient funds!\nYour balance is ₹.{account_data[self.account_number]['balance']:.2f}")
            else:
                messagebox.showerror("Invalid Account", "The recipient account does not exist.")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid transfer amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= account_data[self.account_number]["balance"]:
                # Update the balance in the account_data dictionary
                account_data[self.account_number]["balance"] -= amount
                self.update_balance_label()

                # Record the withdrawal in transfer history
                if self.account_number not in transfer_history:
                    transfer_history[self.account_number] = []
                transfer_history[self.account_number].append(f"Withdrew ₹.{amount:.2f}")

                messagebox.showinfo("Withdrawal", f"₹.{amount:.2f} withdrawn successfully!\nCurrent Balance: ₹.{account_data[self.account_number]['balance']:.2f}")
            else:
                messagebox.showerror("Insufficient Funds", f"Insufficient funds!\nYour balance is ₹.{account_data[self.account_number]['balance']:.2f}")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid withdrawal amount.")

    def check_balance(self):
        # Retrieve the balance from the account_data dictionary
        balance = account_data[self.account_number]["balance"]
        messagebox.showinfo("Balance", f"Available Balance: ₹.{balance:.2f}")

    def view_transfer_history(self):
        if self.account_number in transfer_history:
            history = transfer_history[self.account_number]
            history_text = "\n".join(history)
            messagebox.showinfo("Transfer History", f"Transfer History for Account {self.account_number}:\n\n{history_text}")
        else:
            messagebox.showinfo("Transfer History", "No transfer history available for this account.")

    def update_balance_label(self):
        self.balance_value_label.config(text=f"₹.{account_data[self.account_number]['balance']:.2f}")

print("*******WELCOME TO BANK OF STUDENTS*******")

atm = ATM()
tk.mainloop()
