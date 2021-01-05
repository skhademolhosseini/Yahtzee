"""
Testing roll_5_dice from yahtzee.py
"""

from unittest import TestCase
from unittest.mock import patch

from yahtzee import roll_dice


class TestRoll5Dice(TestCase):

    @patch('random.randint', side_effect=[3])
    def test_roll_dice_1_die(self, mock_random):
        actual = roll_dice(1)
        expected = [3]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3, 5])
    def test_roll_dice_2_dice(self, mock_random):
        actual = roll_dice(2)
        expected = [3, 5]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3, 5, 4, 4, 6, 1, 1])
    def test_roll_dice_7_dice(self, mock_random):
        actual = roll_dice(7)
        expected = [1, 1, 3, 4, 4, 5, 6]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2, 2, 3, 3, 4])
    def test_roll_dice_5_dice_random_already_sorted(self, mock_random):
        actual = roll_dice(5)
        expected = [2, 2, 3, 3, 4]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2, 3, 2, 4, 3])
    def test_roll_dice_5_dice_random_unsorted(self, mock_random):
        actual = roll_dice(5)
        expected = [2, 2, 3, 3, 4]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2, 2, 2, 2, 2])
    def test_roll_dice_5_dice_random_numbers_are_the_same(self, mock_random):
        actual = roll_dice(5)
        expected = [2, 2, 2, 2, 2]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 3, 2, 4, 6])
    def test_roll_dice_5_dice_random_numbers_are_different(self, mock_random):
        actual = roll_dice(5)
        expected = [1, 2, 3, 4, 6]
        self.assertEqual(expected, actual)
