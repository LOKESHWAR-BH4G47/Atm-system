import random
import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

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

    def transaction(self):
        root = tk.Tk()
        root.title("ATM Transaction")

        def show_account_detail():
            self.account_detail()

        def show_balance():
            self.check_balance()

        def deposit_funds():
            amount_str = amount_entry.get()
            if amount_str.strip().replace(".", "").isdigit():
                 amount = float(amount_str)
                 self.deposit(amount)
            else:
                 messagebox.showerror("Invalid Amount", "Please enter a valid amount.")


        def withdraw_funds():
            try:
                amount = float(amount_entry.get())
                self.withdraw(amount)
            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid amount.")

        root.geometry("400x400")

        title_label = tk.Label(root, text="Welcome to Bank of Bhutan", font=("Helvetica", 16))
        title_label.pack(pady=10)

        detail_button = tk.Button(root, text="Account Detail", command=show_account_detail)
        detail_button.pack(pady=10)

        balance_button = tk.Button(root, text="Check Balance", command=show_balance)
        balance_button.pack(pady=10)

        deposit_label = tk.Label(root, text="Enter deposit amount (Nu.):")
        deposit_label.pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()
        deposit_button = tk.Button(root, text="Deposit", command=deposit_funds)
        deposit_button.pack()

        withdraw_label = tk.Label(root, text="Enter withdrawal amount (Nu.):")
        withdraw_label.pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()
        withdraw_button = tk.Button(root, text="Withdraw", command=withdraw_funds)
        withdraw_button.pack()

        balance_label = tk.Label(root, text="Current Balance:", font=("Helvetica", 12))
        balance_label.pack(pady=10)
        balance_value_label = tk.Label(root, text=f"Nu.{self.balance:.2f}", font=("Helvetica", 12))
        balance_value_label.pack()

        exit_button = tk.Button(root, text="Exit", command=root.quit)
        exit_button.pack(pady=10)

        def update_balance_label():
            balance_value_label.config(text=f"Nu.{self.balance:.2f}")

        self.update_balance_label = update_balance_label

        root.mainloop()

print("*******WELCOME TO BANK OF BHUTAN*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")

atm = ATM(name, account_number)

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
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
