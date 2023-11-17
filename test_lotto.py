import unittest
from lotto import lottery_numbers

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

if __name__ == "__main__":
    unittest.main()
