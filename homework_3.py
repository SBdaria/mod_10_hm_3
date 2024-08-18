from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(10):
            plus = randint(50, 500)
            self.balance += plus
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {plus}. Баланс: {self.balance}\n')
            sleep(0.001)

    def take(self):
        for _ in range(10):
            minus = randint(50, 500)
            print(f'Запрос на {minus}')
            if minus <= self.balance:
                self.balance -= minus
                print(f'Снятие: {minus}. Баланс: {self.balance}\n')
            else:
                print('Запрос отклонён, недостаточно средств\n')
                self.lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
