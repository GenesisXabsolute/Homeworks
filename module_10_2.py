from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        num = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while num > 0:
            sleep(1)
            days += 1
            num -= self.power
            print(f'{self.name} сражается {days} день(дня)..., осталось {num} войнов.\n')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все сражения закончились!')


