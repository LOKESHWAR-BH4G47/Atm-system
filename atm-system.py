import tkinter as tk
from tkinter import messagebox

# Define a dictionary to store account numbers, PINs, usernames, and passwords (for demonstration purposes)
# You should replace this with a secure authentication mechanism (e.g., database)
account_data = {
    "123456": {"pin": "1234"},
    "789012": {"pin": "5678"},
}

class ATM:
    def __init__(self):
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
        if account_number in account_data and account_data[account_number]["pin"] == pin :
            self.login_window.destroy()
            self.create_main_window(account_number)
        else:
            messagebox.showerror("Authentication Failed", "Invalid account information. Please try again.")

    def create_main_window(self, account_number):
        self.main_window = tk.Tk()
        self.main_window.title("ATM Machine")
        self.main_window.configure(bg='#2a1b3d')

        bank_name_label = tk.Label(self.main_window, text="Bank of Students", font=("Helvetica", 90, "bold"), bg='#2a1b3d', fg='#44318d')
        bank_name_label.pack(pady=10)

        self.create_transaction_ui(account_number)

    def create_transaction_ui(self, account_number):
        def show_account_detail():
            self.account_detail(account_number)

        def show_balance():
            self.check_balance(account_number)

        def deposit_funds():
            amount_str = deposit_amount_entry.get()
            try:
                amount = float(amount_str)
                self.deposit(account_number, amount)
            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid amount.")

        def withdraw_funds():
            amount_str = withdraw_amount_entry.get()
            try:
                amount = float(amount_str)
                self.withdraw(account_number, amount)
            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid amount.")

        # Use relief='raised' to create 3D-like buttons
        detail_button = tk.Button(self.main_window, text="Account Detail", relief='raised', command=show_account_detail, padx=50, bg='#1f2833', fg='white')
        detail_button.pack(side='left', pady=10, padx=50)

        balance_button = tk.Button(self.main_window, text="Check Balance", relief='raised', command=show_balance, padx=50, bg='#1f2833', fg='white')
        balance_button.pack(side='right', padx=50, pady=10)

        name_label = tk.Label(self.main_window, text=f"Account Number: {account_number}", font=("Helvetica", 12), bg='#1f2833', fg='white')
        name_label.pack(pady=10)

        deposit_label = tk.Label(self.main_window, text="Enter deposit amount (₹.):", bg='#1f2833', fg='white')
        deposit_label.pack()
        deposit_amount_entry = tk.Entry(self.main_window, bg='#a4b3b6', fg='black', borderwidth=5)
        deposit_amount_entry.pack()
        deposit_button = tk.Button(self.main_window, text="Deposit", relief='raised', command=deposit_funds, bg='#1f2833', fg='white')
        deposit_button.pack()

        withdraw_label = tk.Label(self.main_window, text="Enter withdrawal amount (₹.):", bg='#1f2833', fg='white')
        withdraw_label.pack()
        withdraw_amount_entry = tk.Entry(self.main_window, bg='#a4b3b6', fg='black', borderwidth=5, width=20)
        withdraw_amount_entry.pack()
        withdraw_button = tk.Button(self.main_window, text="Withdraw", relief='raised', command=withdraw_funds, bg='#1f2833', fg='white')
        withdraw_button.pack()

        balance_label = tk.Label(self.main_window, text="Current Balance:", font=("Helvetica", 12), bg='#1f2833', fg='white')
        balance_label.pack(pady=20)
        self.balance_value_label = tk.Label(self.main_window, text=f"₹.{self.balance:.2f}", font=("Helvetica", 12), bg='#1f2833', fg='white')
        self.balance_value_label.pack()

        exit_button = tk.Button(self.main_window, text="Exit", relief='raised', command=self.main_window.destroy, bg='#1f2833', fg='white')
        exit_button.pack(pady=10)

    def account_detail(self, account_number):
        # Retrieve account details from the account_data dictionary
        username = account_data[account_number]["username"]
        balance = self.balance

        messagebox.showinfo("Account Detail", f"Account Number: {account_number}\nUsername: {username}\nAvailable Balance: ₹.{balance:.2f}")

    def deposit(self, account_number, amount):
        if amount > 0:
            # Update the balance in the account_data dictionary
            self.balance += amount
            account_data[account_number]["balance"] = self.balance
            self.update_balance_label()
            messagebox.showinfo("Deposit", f"₹.{amount:.2f} deposited successfully!\nCurrent Balance: ₹.{self.balance:.2f}")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid deposit amount.")

    def withdraw(self, account_number, amount):
        if amount > 0:
            if amount <= self.balance:
                # Update the balance in the account_data dictionary
                self.balance -= amount
                account_data[account_number]["balance"] = self.balance
                self.update_balance_label()
                messagebox.showinfo("Withdrawal", f"₹.{amount:.2f} withdrawn successfully!\nCurrent Balance: ₹.{self.balance:.2f}")
            else:
                messagebox.showerror("Insufficient Funds", f"Insufficient funds!\nYour balance is ₹.{self.balance:.2f}")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid withdrawal amount.")

    def check_balance(self, account_number):
        # Retrieve the balance from the account_data dictionary
        balance = account_data[account_number]["balance"]
        messagebox.showinfo("Balance", f"Available Balance: ₹.{balance:.2f}")

    def update_balance_label(self):
        self.balance_value_label.config(text=f"₹.{self.balance:.2f}")

    def run_transaction(self):
        self.main_window.mainloop()

print("*******WELCOME TO BANK OF Students*******")

atm = ATM()

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.run_transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command! Enter 'y' for yes and 'n' for NO.\n")