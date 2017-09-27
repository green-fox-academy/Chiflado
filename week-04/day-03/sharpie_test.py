import unittest
from sharpie import Sharpie

class ShaprieTest(unittest.TestCase):

    def test_use(self):
        test_use = Sharpie('color', 1)
        self.assertEqual(test_use.use(), Sharpie('color', 1).ink_amount - 0.5)



if __name__ == '__main__':
    unittest.main()