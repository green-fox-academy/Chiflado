import unittest
from Balazs_work import Apple

class AppleTest(unittest.TestCase):
    def test_get_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), 'apple')

    def test_get_sum(self):
        test_sum = Apple()
        self.assertEqual(test_sum.get_sum([1,2,3]), 6)

    def test_get_sum_empty(self):
        test_sum = Apple()
        self.assertEqual(test_sum.get_sum([]), 0)        

    def test_get_sum_one(self):
        test_sum = Apple()
        self.assertEqual(test_sum.get_sum([1]), 1)

    def test_get_sum_null(self):
        test_sum = Apple()
        self.assertEqual(test_sum.get_sum([0]), 0)

    def test_get_anagram_true(self):
        test_get_anagram = Apple()
        self.assertTrue(test_get_anagram.get_anagram('abcd', 'cdab'))

    def test_get_anagram_false(self):
        test_get_anagram = Apple()
        self.assertFalse(test_get_anagram.get_anagram('abcd', 'cjab'))

    def test_letter_counter_empty(self):
        test_letter_counter = Apple()
        self.assertEqual(test_letter_counter.letter_counter(''), {})



if __name__ == '__main__':
    unittest.main()