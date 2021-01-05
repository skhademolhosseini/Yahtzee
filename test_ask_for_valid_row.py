"""
Testing ask_for_valid_row from yahtzee.py
"""

from unittest import TestCase
from unittest.mock import patch

from yahtzee import ask_for_valid_row


class TestAskForValidRow(TestCase):

    @patch('builtins.input', side_effect=["4"])
    def test_ask_for_valid_row_first_input_is_valid(self):
        actual = ask_for_valid_row()
        expected = "4"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["yes", "2"])
    def test_ask_for_valid_row_second_input_is_valid(self):
        actual = ask_for_valid_row()
        expected = "2"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["yes", "Full House", "12"])
    def test_ask_for_valid_row_third_input_is_valid(self):
        actual = ask_for_valid_row()
        expected = "12"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["7", "5"])
    def test_ask_for_valid_row_first_input_is_invalid_numeric_character_second_input_is_valid(self):
        actual = ask_for_valid_row()
        expected = "5"
        self.assertEqual(expected, actual)
