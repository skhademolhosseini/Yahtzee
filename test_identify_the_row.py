"""
Testing identify_the_row from yahtzee.py
"""

from unittest import TestCase

from yahtzee import identify_the_row


class TestIdentifyTheRow(TestCase):

    def test_identify_the_row_selected_row_is_1(self):
        valid_selected_row = "1"
        actual = identify_the_row(valid_selected_row)
        expected = "Aces"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_2(self):
        valid_selected_row = "2"
        actual = identify_the_row(valid_selected_row)
        expected = "Twos"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_3(self):
        valid_selected_row = "3"
        actual = identify_the_row(valid_selected_row)
        expected = "Threes"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_4(self):
        valid_selected_row = "4"
        actual = identify_the_row(valid_selected_row)
        expected = "Fours"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_5(self):
        valid_selected_row = "5"
        actual = identify_the_row(valid_selected_row)
        expected = "Fives"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_6(self):
        valid_selected_row = "6"
        actual = identify_the_row(valid_selected_row)
        expected = "Sixes"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_10(self):
        valid_selected_row = "10"
        actual = identify_the_row(valid_selected_row)
        expected = "3 of a kind"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_11(self):
        valid_selected_row = "11"
        actual = identify_the_row(valid_selected_row)
        expected = "4 of a kind"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_12(self):
        valid_selected_row = "12"
        actual = identify_the_row(valid_selected_row)
        expected = "Full House"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_13(self):
        valid_selected_row = "13"
        actual = identify_the_row(valid_selected_row)
        expected = "Small Straight"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_14(self):
        valid_selected_row = "14"
        actual = identify_the_row(valid_selected_row)
        expected = "Large Straight"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_15(self):
        valid_selected_row = "15"
        actual = identify_the_row(valid_selected_row)
        expected = "YAHTZEE"
        self.assertEqual(expected, actual)

    def test_identify_the_row_selected_row_is_16(self):
        valid_selected_row = "16"
        actual = identify_the_row(valid_selected_row)
        expected = "Chance"
        self.assertEqual(expected, actual)
