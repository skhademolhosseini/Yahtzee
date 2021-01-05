"""
Testing four_of_a_kind from yahtzee.py
"""

from unittest import TestCase

from yahtzee import four_of_a_kind_score_calculator


class TestFourOfaKindScoreCalculator(TestCase):

    def test_four_of_a_kind_score_calculator_more_than_four_of_a_kind(self):
        dice_list = [5, 5, 5, 5, 5]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 25
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_score_calculator_not_a_four_of_a_kind(self):
        dice_list = [2, 3, 5, 5, 5]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_score_calculator_four_of_a_kind_of_aces(self):
        dice_list = [1, 1, 1, 1, 5]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 9
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_score_calculator_four_of_a_kind_of_twos(self):
        dice_list = [2, 2, 2, 2, 4]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 12
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_score_calculator_four_of_a_kind_of_threes(self):
        dice_list = [3, 3, 3, 3, 6]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 18
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_score_calculator_four_of_a_kind_of_fours(self):
        dice_list = [3, 4, 4, 4, 4]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 19
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_score_calculator_four_of_a_kind_of_fives(self):
        dice_list = [1, 5, 5, 5, 5]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 21
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_score_calculator_four_of_a_kind_of_sixes(self):
        dice_list = [5, 6, 6, 6, 6]
        actual = four_of_a_kind_score_calculator(dice_list)
        expected = 29
        self.assertEqual(expected, actual)
