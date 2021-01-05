"""
Testing large_straight_score_calculator from yahtzee.py
"""

from unittest import TestCase

from yahtzee import large_straight_score_calculator


class TestLargeStraightScoreCalculator(TestCase):

    def test_large_straight_score_calculator_not_a_large_straight(self):
        dice_list = [2, 2, 3, 6, 6]
        actual = large_straight_score_calculator(dice_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test_large_straight_score_calculator_it_is_a_small_straight(self):
        dice_list = [1, 2, 3, 4, 6]
        actual = large_straight_score_calculator(dice_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test_large_straight_score_calculator_large_straight_1(self):
        dice_list = [1, 2, 3, 4, 5]
        actual = large_straight_score_calculator(dice_list)
        expected = 40
        self.assertEqual(expected, actual)

    def test_large_straight_score_calculator_large_straight_2(self):
        dice_list = [2, 3, 4, 5, 6]
        actual = large_straight_score_calculator(dice_list)
        expected = 40
        self.assertEqual(expected, actual)
