"""
Testing full_house_core_calculator from yahtzee.py
"""

from unittest import TestCase

from yahtzee import full_house_score_calculator


class TestFullHouseScoreCalculator(TestCase):

    def test_full_house_score_calculator_three_of_a_kind_of_the_smaller_number_and_pair_of_the_greater_number(self):
        dice_list = [2, 2, 2, 5, 5]
        actual = full_house_score_calculator(dice_list)
        expected = 25
        self.assertEqual(expected, actual)

    def test_full_house_score_calculator_three_of_a_kind_of_the_greater_number_and_pair_of_the_smaller_number(self):
        dice_list = [4, 4, 6, 6, 6]
        actual = full_house_score_calculator(dice_list)
        expected = 25
        self.assertEqual(expected, actual)

    def test_full_house_score_calculator_five_of_a_kind(self):
        dice_list = [3, 3, 3, 3, 3]
        actual = full_house_score_calculator(dice_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test_full_house_score_calculator_not_a_full_house(self):
        dice_list = [1, 2, 2, 5, 5]
        actual = full_house_score_calculator(dice_list)
        expected = 0
        self.assertEqual(expected, actual)
