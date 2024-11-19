from unittest import TestCase
from _12_1 import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        human = Runner("Человек")
        for i in range(10):
            human.walk()
        self.assertEqual(human.distance, 50)

    def test_run(self):
        human = Runner("Человек")
        for i in range(10):
            human.run()
        self.assertEqual(human.distance, 100)

    def test_challenge(self):
        bro = Runner("Б1")
        bro_2 = Runner("Б2")
        for i in range(10):
            bro.run()
            bro_2.walk()
        self.assertNotEqual(bro.distance, bro_2.distance)
