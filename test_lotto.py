import unittest
from .lotto import lottery_numbers

class TestLotteryNumbers(unittest.TestCase):

  def test_lottery_numbers_amount_valid(self):
        result = lottery_numbers(1, 1, 100)
        self.assertEqual(len(result), 1)

if __name__ == "__main__":
    unittest.main()
