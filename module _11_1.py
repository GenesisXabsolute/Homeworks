import time
import threading
import queue


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:

    def __init__(self, queue, tables):
        self.queue = queue
        self.tables = tables

    def customer_arrival(self):
        total_customer = 20  # хватит и 20 посетителей в кафе
        for num_cust in range(1, total_customer + 1):
            print(f'Посетитель номер {num_cust} прибыл.')
            self.serve_customer(num_cust)
            time.sleep(2)

    def serve_customer(self, num_cust):
        check_table = False
        for table in tables:
            if not table.is_busy:  # если стол не занят
                somebody = Customer(num_cust, self, table)  # запуск потока (начинается обслуживание)
                table.is_busy = True
                somebody.start()
                check_table = True
                break
        if not check_table:  # если стол занят
            self.queue.put(num_cust)  # берем в очередь и закидываем туда кто-бы это ни был
            print(f'Посетитель {num_cust} ожидает свободный стол!')


class Customer(threading.Thread):
    def __init__(self, visitor, cafe, table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.visitor = visitor
        self.cafe = cafe
        self.table = table

    def run(self):
        self.table.is_busy = True
        print(f'Посетитель номер {self.visitor} сел за стол {self.table.number}. (начало обслуживания)')
        time.sleep(5)
        print(f'Посетитель номер {self.visitor} покушал и ушёл. (конец обслуживания)')
        self.table.is_busy = False
        if self.cafe.queue.qsize() > 0:
            self.cafe.serve_customer(self.cafe.queue.get())


# Создаем столики в кафе
table1 = Table(1)  # cоздали первый столик
table2 = Table(2)  # cоздали второй столик
table3 = Table(3)  # cоздали третий  столик
tables = [table1, table2, table3]

# Инициализируем кафе
queue = queue.Queue()  # создали одну большую очередь
queue.qsize()  # возвращает примерный размер очереди.
# Обратите внимание, что SimpleQueue.qsize() > 0
# не гарантирует, что последующий метод
# Queue.get() не будет блокироваться.
cafe = Cafe(queue, tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
