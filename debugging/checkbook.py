#!/usr/bin/env python3

"""
Simple Checkbook CLI module.

This module provides a `Checkbook` class to track a monetary balance and a
small interactive `main()` function to deposit, withdraw and display the
current balance from the command line.

The interactive program validates user input and handles invalid values
gracefully to prevent crashes.
"""


class Checkbook:
    """
    Checkbook ledger for a single account.

    Function description:
        Maintain an account balance and provide methods to deposit,
        withdraw and retrieve the current balance.

    Parameters:
        This class has no initialization parameters.

    Returns:
        An instance of `Checkbook` with a `balance` attribute.
    """

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
            Add funds to the checkbook balance.

        Parameters:
            amount (float): Amount to deposit; must be > 0.

        Returns:
            None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
            Withdraw funds from the checkbook balance if sufficient.

        Parameters:
            amount (float): Amount to withdraw; must be > 0 and <= balance.

        Returns:
            None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
            Print the current account balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        cmd = action.strip().lower()
        if cmd == 'exit':
            break
        elif cmd == 'deposit':
            try:
                amount_str = input("Enter the amount to deposit: $")
            except (EOFError, KeyboardInterrupt):
                print("\nCancelled.")
                continue
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            cb.deposit(amount)
        elif cmd == 'withdraw':
            try:
                amount_str = input("Enter the amount to withdraw: $")
            except (EOFError, KeyboardInterrupt):
                print("\nCancelled.")
                continue
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            cb.withdraw(amount)
        elif cmd == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
