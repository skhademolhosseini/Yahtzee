from unittest import TestCase
from unittest.mock import patch

from yahtzee import get_valid_dice


class TestGetValidDice(TestCase):

    @patch('builtins.input', side_effect=["1 2 4"])
    def test_get_valid_dice_first_time_valid(self, mock_input):
        actual = get_valid_dice()
        expected = ["1", "2", "4"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1 8 4", "1 5"])
    def test_get_valid_dice_second_time_valid(self, mock_input):
        actual = get_valid_dice()
        expected = ["1", "5"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["15", "1 5"])
    def test_get_valid_dice_first_time_no_space_second_time_valid(self, mock_input):
        actual = get_valid_dice()
        expected = ["1", "5"]
        self.assertEqual(expected, actual)
