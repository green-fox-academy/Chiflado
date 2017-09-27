import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):

    def test_eat(self):
        test_eat = Animal()
        self.assertEqual(test_eat.eat(), Animal.hunger - 1)

    def test_drink(self):
        test_drink = Animal()
        self.assertEqual(test_drink.drink(), Animal.thirst - 1)

    def test_play(self):
        test_play = Animal()
        self.assertEquals(test_play.play(), (Animal.thirst + 1, Animal.hunger + 1))


if __name__ == '__main__':
    unittest.main()