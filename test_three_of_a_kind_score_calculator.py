"""
Testing three_of_a_kind_score_calculator from yahtzee.py
"""

from unittest import TestCase

from yahtzee import three_of_a_kind_score_calculator


class TestThreeOfaKindScoreCalculator(TestCase):

    def test_three_of_a_kind_score_calculator_more_than_3_of_a_kind(self):
        dice_list = [2, 5, 5, 5, 5]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 22
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_score_calculator_but_it_is_not_a_3_of_a_kind(self):
        dice_list = [2, 2, 4, 5, 5]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_score_calculator_3_of_a_kind_of_aces(self):
        dice_list = [1, 1, 1, 2, 3]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 8
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_score_calculator_3_of_a_kind_of_twos(self):
        dice_list = [1, 2, 2, 2, 3]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 10
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_score_calculator_3_of_a_kind_of_threes(self):
        dice_list = [1, 3, 3, 3, 4]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 14
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_score_calculator_3_of_a_kind_of_fours(self):
        dice_list = [1, 4, 4, 4, 6]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 19
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_score_calculator_3_of_a_kind_of_fives(self):
        dice_list = [1, 1, 5, 5, 5]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 17
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_score_calculator_3_of_a_kind_of_sixes(self):
        dice_list = [3, 3, 6, 6, 6]
        actual = three_of_a_kind_score_calculator(dice_list)
        expected = 24
        self.assertEqual(expected, actual)
