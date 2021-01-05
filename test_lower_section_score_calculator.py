"""
Testing score_calculator from yahtzee.py
Helper functions used in this function have their own unittests.
"""

from unittest import TestCase

from yahtzee import lower_section_score_calculator


class TestLowerSectionScoreCalculator(TestCase):

    def test_lower_section_score_calculator_3_of_a_kind(self):
        dice_list = [1, 2, 2, 2, 6]
        actual = lower_section_score_calculator(dice_list, "10")
        expected = 13
        self.assertEqual(expected, actual)

    def test_lower_section_score_calculator_4_of_a_kind(self):
        dice_list = [2, 4, 4, 4, 4]
        actual = lower_section_score_calculator(dice_list, "11")
        expected = 18
        self.assertEqual(expected, actual)

    def test_lower_section_score_calculator_full_house(self):
        dice_list = [2, 2, 4, 4, 4]
        actual = lower_section_score_calculator(dice_list, "12")
        expected = 25
        self.assertEqual(expected, actual)

    def test_lower_section_score_calculator_small_straight(self):
        dice_list = [1, 2, 3, 3, 4]
        actual = lower_section_score_calculator(dice_list, "13")
        expected = 30
        self.assertEqual(expected, actual)

    def test_lower_section_score_calculator_large_straight(self):
        dice_list = [1, 2, 3, 4, 5]
        actual = lower_section_score_calculator(dice_list, "14")
        expected = 40
        self.assertEqual(expected, actual)

    def test_lower_section_score_calculator_chance(self):
        dice_list = [2, 2, 3, 4, 4]
        actual = lower_section_score_calculator(dice_list, "16")
        expected = 15
        self.assertEqual(expected, actual)

    def test_lower_section_score_calculator_getting_0(self):
        dice_list = [2, 2, 4, 4, 4]
        actual = lower_section_score_calculator(dice_list,"14")
        expected = 0
        self.assertEqual(expected, actual)
