import unittest
from Balazs_work import Apple

class AppleTest(unittest.TestCase):
    def test_get_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), 'apple')


if __name__ == '__main__':
    unittest.main()