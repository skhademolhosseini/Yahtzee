"""
Testing re_roll_selected_dice from yahtzee.py
"""

from unittest import TestCase
from unittest.mock import patch

from yahtzee import re_roll_selected_dice


class TestReRollSelectedDice(TestCase):

    @patch('random.randint', side_effect=[6, 3, 3, 4])
    def test_re_roll_selected_dice_4_selected_dice(self, mock_random_number):
        dice_list = [1, 1, 1, 1, 1]
        selected_dice = [1, 3, 4, 5]
        re_roll_selected_dice(dice_list, selected_dice)
        expected = [1, 3, 3, 4, 6]
        self.assertEqual(expected, dice_list)

    @patch('random.randint', side_effect=[2, 2, 4])
    def test_re_roll_selected_dice_3_selected_dice(self, mock_random_number):
        dice_list = [1, 1, 1, 1, 1]
        selected_dice = [1, 3, 5]
        re_roll_selected_dice(dice_list, selected_dice)
        expected = [1, 1, 2, 2, 4]
        self.assertEqual(expected, dice_list)

    @patch('random.randint', side_effect=[6, 5])
    def test_re_roll_selected_dice_2_selected_dice(self, mock_random_number):
        dice_list = [1, 1, 1, 1, 1]
        selected_dice = [1, 2]
        re_roll_selected_dice(dice_list, selected_dice)
        expected = [1, 1, 1, 5, 6]
        self.assertEqual(expected, dice_list)

    @patch('random.randint', side_effect=[2, 2, 2])
    def test_re_roll_selected_dice_3_selected_dice_get_same_face_value(self, mock_random_number):
        dice_list = [2, 2, 2, 2, 2]
        selected_dice = [1, 3, 4]
        re_roll_selected_dice(dice_list, selected_dice)
        expected = [2, 2, 2, 2, 2]
        self.assertEqual(expected, dice_list)

    @patch('random.randint', side_effect=[3, 6, 1])
    def test_re_roll_selected_dice_random_starting_dice_list_and_3_selected_dice(self, mock_random_number):
        dice_list = [2, 4, 4, 5, 6]
        selected_dice = [1, 2, 4]
        re_roll_selected_dice(dice_list, selected_dice)
        expected = [1, 3, 4, 6, 6]
        self.assertEqual(expected, dice_list)
