"""
Testing chance_score_calculator from yahtzee.py
"""

from unittest import TestCase

from yahtzee import chance_score_calculator


class TestChanceScoreCalculator(TestCase):

    def test_chance_score_calculator_dice_list_is_not_special(self):
        dice_list = [1, 3, 3, 4, 6]
        actual = chance_score_calculator(dice_list)
        expected = 17
        self.assertEqual(expected, actual)

    def test_chance_score_calculator_dice_list_is_4_of_a_kind(self):
        dice_list = [3, 3, 3, 3, 6]
        actual = chance_score_calculator(dice_list)
        expected = 18
        self.assertEqual(expected, actual)

    def test_chance_score_calculator_dice_list_is_full_house(self):
        dice_list = [1, 1, 1, 3, 3]
        actual = chance_score_calculator(dice_list)
        expected = 9
        self.assertEqual(expected, actual)

    def test_chance_score_calculator_dice_list_is_straight(self):
        dice_list = [1, 2, 3, 4, 5]
        actual = chance_score_calculator(dice_list)
        expected = 15
        self.assertEqual(expected, actual)

    def test_chance_score_calculator_dice_list_is_yahtzee(self):
        dice_list = [2, 2, 2, 2, 2]
        actual = chance_score_calculator(dice_list)
        expected = 10
        self.assertEqual(expected, actual)
