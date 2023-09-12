import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.create_main_window()

    def create_main_window(self):
        self.main_window = tk.Tk()
        self.main_window.title("ATM Machine")
        # self.main_window.configure(bg='black')
        self.main_window.configure(bg='#2a1b3d')

        bank_name_label = tk.Label(self.main_window, text="Bank of Students", font=("Helvetica", 90),bg='#2a1b3d',fg='#44318d')
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

        # Use relief='raised' to create 3D-like buttons
        
        detail_button = tk.Button(self.main_window, text="Account Detail", relief='raised', command=show_account_detail,padx=50, bg='#1f2833', fg='white')
        
        detail_button.pack(pady=10)

        balance_button = tk.Button(self.main_window, text="Check Balance", relief='raised', command=show_balance,padx=50, bg='#1f2833', fg='white')
        balance_button.pack(pady=10)

        name_label = tk.Label(self.main_window, text=f"Account Holder: {self.name.upper()}", font=("Helvetica", 12), bg='#1f2833', fg='white')
        name_label.pack(pady=10)

        deposit_label = tk.Label(self.main_window, text="Enter deposit amount (Nu.):", bg='#1f2833', fg='white')
        deposit_label.pack()
        deposit_amount_entry = tk.Entry(self.main_window, bg='#a4b3b6', fg='black',borderwidth=5)
        deposit_amount_entry.pack()
        deposit_button = tk.Button(self.main_window, text="Deposit", relief='raised', command=deposit_funds, bg='#1f2833', fg='white')
        deposit_button.pack()

        withdraw_label = tk.Label(self.main_window, text="Enter withdrawal amount (Nu.):", bg='#1f2833', fg='white')
        withdraw_label.pack()
        withdraw_amount_entry = tk.Entry(self.main_window, bg='#a4b3b6', fg='black',borderwidth=5,width=20)
        withdraw_amount_entry.pack()
        withdraw_button = tk.Button(self.main_window, text="Withdraw", relief='raised', command=withdraw_funds, bg='#1f2833', fg='white')
        withdraw_button.pack()

        balance_label = tk.Label(self.main_window, text="Current Balance:", font=("Helvetica", 12), bg='#1f2833', fg='white')
        balance_label.pack(pady=50)
        self.balance_value_label = tk.Label(self.main_window, text=f"Nu.{self.balance:.2f}", font=("Helvetica", 12), bg='#1f2833', fg='white')
        self.balance_value_label.pack()

        exit_button = tk.Button(self.main_window, text="Exit", relief='raised', command=self.main_window.destroy, bg='#1f2833', fg='white')
        exit_button.pack(pady=10)

    def account_detail(self):
        messagebox.showinfo("Account Detail", f"Account Holder: {self.name.upper()}\nAccount Number: {self.account_number}\nAvailable Balance: Nu.{self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.update_balance_label()
            messagebox.showinfo("Deposit", f"Nu.{amount:.2f} deposited successfully!\nCurrent Balance: Nu.{self.balance:.2f}")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.update_balance_label()
                messagebox.showinfo("Withdrawal", f"Nu.{amount:.2f} withdrawn successfully!\nCurrent Balance: Nu.{self.balance:.2f}")
            else:
                messagebox.showerror("Insufficient Funds", f"Insufficient funds!\nYour balance is Nu.{self.balance:.2f}")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid withdrawal amount.")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Available Balance: Nu.{self.balance:.2f}")

    def update_balance_label(self):
        self.balance_value_label.config(text=f"Nu.{self.balance:.2f}")

    def run_transaction(self):
        self.main_window.mainloop()

print("*******WELCOME TO BANK OF LR*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")

atm = ATM(name, account_number)

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
