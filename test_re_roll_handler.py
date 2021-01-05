"""
Testing re_roll_handler from yahtzee.py
"""

from unittest import TestCase
from unittest.mock import patch

from yahtzee import re_roll_handler


class TestReRollHandler(TestCase):

    @patch('builtins.input', side_effect=["no"])
    def test_re_roll_handler_no_re_roll(self, mock_input):
        dice_list = [1, 2, 3, 4, 5]
        re_roll_handler(dice_list)
        expected_new_dice_list = [1, 2, 3, 4, 5]
        self.assertEqual(expected_new_dice_list, dice_list)

    @patch('builtins.input', side_effect=["yes", "1 3 4", "no"])
    @patch('random.randint', side_effect=[2, 6, 3])
    def test_re_roll_handler_1_set_of_re_roll_re_rolling_first_third_and_forth_dice(self, mock_random,mock_input):
        dice_list = [1, 2, 3, 4, 5]
        re_roll_handler(dice_list)
        expected_new_dice_list = [2, 2, 3, 5, 6]
        self.assertEqual(expected_new_dice_list, dice_list)

    @patch('builtins.input', side_effect=["yes", "1 3 4", "yes", "1 5"])
    @patch('random.randint', side_effect=[2, 6, 3, 6, 6])
    def test_re_roll_handler_2_set_of_re_rolls_first_re_rolling_first_third_and_forth_dice_then_first_and_fifth(self, mock_random, mock_input):
        dice_list = [1, 2, 3, 4, 5]
        re_roll_handler(dice_list)
        expected_new_dice_list = [2, 3, 5, 6, 6]
        self.assertEqual(expected_new_dice_list, dice_list)
