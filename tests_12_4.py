import unittest
import logging

LOG_FILENAME = 'runner_test.log'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO, filemode="w", encoding='UTF-8',
    format="%(asctime)s | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        s = []
        for participant in self.participants:
            s.append(participant.speed)
        s.sort(reverse=True)
        for i in s:
            for participant in self.participants:
                if participant.speed == i:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_walk(self):
        try:
            ds1 = Runner("Ivan", -100)
            for i in range(10):
                ds1.walk()
            logging.info("'test_walk' выполнен успешно")
            self.assertEqual(ds1.distance, 50)
            return ds1.distance
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            self.assertEqual(ds1.distance, 50)
            return ds1.distance

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_run(self):
        try:
            ds2 = Runner(2, 10)
            for i in range(10):
                ds2.run()
            self.assertEqual(ds2.distance, 100)
            logging.info("'test_run' выполнен успешно")
            return ds2.run().distance
        except:
            logging.warning("Неверный тип данных для Runner", exc_info=True)
            self.assertEqual(ds2.distance, 100)
            return ds2.distance

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_challenge(self):
        self.frst_r = Runner(name="Iiigor")
        self.sec_r = Runner(name="Oleg")
        for i in range(10):
            self.frst_r.run()
            self.sec_r.walk()
        self.assertNotEqual(self.frst_r.run, self.sec_r.walk)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        del cls.all_results

    def setUp(self):
        self.run_1 = Runner('Усейн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)
        self.results = {}

    def tearDown(self):
        self.all_results = self.results
        for key in self.all_results:
            print(key, self.all_results[key])
        print('___ ' * 20)
        super().tearDown()

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start1(self):
        d = Tournament(90, self.run_1, self.run_3)
        ds1 = d.start()
        self.results = ds1
        self.assertTrue(self.results[2] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start2(self):
        d = Tournament(90, self.run_2, self.run_3)
        ds2 = d.start()
        self.results = ds2
        self.assertTrue(self.results[2] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start3(self):
        d = Tournament(90, self.run_3, self.run_1, self.run_2)
        ds3 = d.start()
        self.results = ds3
        self.assertTrue(self.results[3] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожеы')
    def test_start4(self):
        """Введен дополнительно """
        d = Tournament(90, self.run_2, self.run_1, self.run_3)
        ds4 = d.start()
        self.results = ds4
        self.assertTrue(self.results[2] == 'Андрей', 'Наличие логической ошибки в методе start')


if __name__ == 'main':
    unittest.main()
