"""
Testing small_straight_score_calculator from yahtzee.py
"""

from unittest import TestCase

from yahtzee import small_straight_score_calculator


class TestSmallStraightScoreCalculator(TestCase):

    def test_small_straight_score_calculator_not_a_small_straight(self):
        dice_list = [1, 2, 2, 3, 3]
        actual = small_straight_score_calculator(dice_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test_small_straight_score_calculator_it_is_a_large_straight(self):
        dice_list = [1, 2, 3, 4, 5]
        actual = small_straight_score_calculator(dice_list)
        expected = 30
        self.assertEqual(expected, actual)

    def test_small_straight_score_calculator_smallest_die_is_1_and_no_duplicates(self):
        dice_list = [1, 3, 4, 5, 6]
        actual = small_straight_score_calculator(dice_list)
        expected = 30
        self.assertEqual(expected, actual)

    def test_small_straight_score_calculator_smallest_die_is_1_and_there_is_a_duplicate(self):
        dice_list = [1, 2, 3, 3, 4]
        actual = small_straight_score_calculator(dice_list)
        expected = 30
        self.assertEqual(expected, actual)

    def test_small_straight_score_calculator_smallest_die_is_2_and_no_duplicates(self):
        dice_list = [2, 3, 4, 5, 6]
        actual = small_straight_score_calculator(dice_list)
        expected = 30
        self.assertEqual(expected, actual)

    def test_small_straight_score_calculator_smallest_die_is_2_and_there_is_a_duplicate(self):
        dice_list = [2, 2, 3, 4, 5]
        actual = small_straight_score_calculator(dice_list)
        expected = 30
        self.assertEqual(expected, actual)

    def test_small_straight_score_calculator_smallest_die_is_3_and_there_is_a_duplicate(self):
        dice_list = [3, 4, 5, 5, 6]
        actual = small_straight_score_calculator(dice_list)
        expected = 30
        self.assertEqual(expected, actual)
