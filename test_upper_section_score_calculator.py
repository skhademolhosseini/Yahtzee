"""
Testing upper_section_score_calculator from yahtzee.py
"""

from unittest import TestCase

from yahtzee import upper_section_score_calculator


class TestUpperSectionScoreCalculator(TestCase):

    def test_upper_section_score_calculator_valid_row_is_1_and_dice_list_has_at_least_one_1(self):
        valid_row = "1"
        dice_list = [1, 1, 1, 3, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 3
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_1_and_dice_list_does_not_have_a_1(self):
        valid_row = "1"
        dice_list = [2, 2, 3, 5, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 0
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_2_and_dice_list_has_at_least_one_2(self):
        valid_row = "2"
        dice_list = [1, 2, 2, 2, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 6
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_2_and_dice_list_does_not_have_a_2(self):
        valid_row = "2"
        dice_list = [1, 1, 3, 5, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 0
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_3_and_dice_list_has_at_least_one_3(self):
        valid_row = "3"
        dice_list = [3, 3, 3, 3, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 12
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_3_and_dice_list_does_not_have_a_3(self):
        valid_row = "3"
        dice_list = [2, 2, 4, 5, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 0
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_4_and_dice_list_has_at_least_one_4(self):
        valid_row = "4"
        dice_list = [1, 1, 4, 4, 5]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 8
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_4_and_dice_list_does_not_have_a_4(self):
        valid_row = "4"
        dice_list = [2, 2, 3, 5, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 0
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_5_and_dice_list_has_at_least_one_5(self):
        valid_row = "5"
        dice_list = [1, 3, 5, 5, 5]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 15
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_5_and_dice_list_does_not_have_a_5(self):
        valid_row = "5"
        dice_list = [2, 2, 3, 4, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 0
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_6_and_dice_list_has_at_least_one_6(self):
        valid_row = "6"
        dice_list = [6, 6, 6, 6, 6]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 30
        self.assertEqual(expected, actual)

    def test_upper_section_score_calculator_valid_row_is_6_and_dice_list_does_not_have_a_6(self):
        valid_row = "6"
        dice_list = [2, 2, 3, 5, 5]
        actual = upper_section_score_calculator(dice_list, valid_row)
        expected = 0
        self.assertEqual(expected, actual)
