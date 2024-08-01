import unittest


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


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    @classmethod
    def tearDownClass(cls):
        for i in all_results:
            print(i)

    def test1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        all_results.append(tournament.start())
        result = all_results[-1][2]
        self.assertTrue(self.runner3, result)

    def test2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        all_results.append(tournament.start())
        result = all_results[-1][2]
        self.assertTrue(self.runner3, result)

    def test3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results.append(tournament.start())
        result = all_results[-1][2]
        self.assertTrue(self.runner2, result)


if __name__ == '__main__':
    unittest.main()
