import threading
from threading import Lock

lock1 = Lock()
lock2 = Lock()


class BankAccount:
    def __init__(self):
        self.amount = 1000

    def deposit(self, amount):
        self.amount += amount
        print(f'Deposited {amount}, new balance is {self.amount}')

    def withdraw(self, amount):
        self.amount -= amount
        print(f'Withdrew {amount}, new balance is {self.amount}')


def deposit_task(account, amount):
    lock1.acquire()
    for _ in range(5):
        account.deposit(amount)
    print()
    lock1.release()


def withdraw_task(account, amount):
    lock2.acquire()
    for _ in range(5):
        account.withdraw(amount)
    print()
    lock2.release()


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
