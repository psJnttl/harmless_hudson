import unittest
from lotto import lottery_numbers, joker_numbers

class TestLotteryNumbers(unittest.TestCase):

    def test_lottery_numbers_amount_valid(self):
        result = lottery_numbers(1, 1, 100)
        self.assertEqual(len(result), 1)
        result = lottery_numbers(10, 1, 100)
        self.assertEqual(len(result), 10)
        result = lottery_numbers(100, 1, 100)
        self.assertEqual(len(result), 100)
        result = lottery_numbers(1000, 1, 1000)
        self.assertEqual(len(result), 1000)

    def test_lottery_numbers_unique(self):
        result = lottery_numbers(10, 1, 10)
        self.assertEqual(len(set(result)), 10)
        result = lottery_numbers(100, 1, 100)
        self.assertEqual(len(set(result)), 100)
        result = lottery_numbers(1000, 1, 1000)
        self.assertEqual(len(set(result)), 1000)

    def test_lottery_numbers_valid_range(self):
        result = lottery_numbers(2, 1, 2)
        self.assertTrue(all(1 <= x <= 2 for x in result))
        result = lottery_numbers(10, 1, 100)
        self.assertTrue(all(1 <= x <= 100 for x in result))
        result = lottery_numbers(10, -100, 0)
        self.assertTrue(all(-100 <= x <= 0 for x in result))

    def test_joker_numbers_length(self):
        numbers = joker_numbers()
        self.assertEqual(len(numbers), 7)

    def test_joker_numbers_range(self):
        numbers = joker_numbers()
        for number in numbers:
            self.assertTrue(0 <= number <= 9)

if __name__ == "__main__":
    unittest.main()
