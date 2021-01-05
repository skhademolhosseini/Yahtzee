"""
Testing print_dice from yahtzee.py
"""

from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import print_dice


class TestPrintDice(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_5_different_dice(self, mock_output):
        dice_list = [2, 3, 4, 5, 6]
        print_dice(dice_list)
        expected_print = "Current dice:\nDie 1: 2\nDie 2: 3\nDie 3: 4\nDie 4: 5\nDie 5: 6\n"
        self.assertEqual(expected_print, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_5_same_dice(self, mock_output):
        dice_list = [3, 3, 3, 3, 3]
        print_dice(dice_list)
        expected_print = "Current dice:\nDie 1: 3\nDie 2: 3\nDie 3: 3\nDie 4: 3\nDie 5: 3\n"
        self.assertEqual(expected_print, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_5_random_dice(self, mock_output):
        dice_list = [1, 1, 4, 4, 5]
        print_dice(dice_list)
        expected_print = "Current dice:\nDie 1: 1\nDie 2: 1\nDie 3: 4\nDie 4: 4\nDie 5: 5\n"
        self.assertEqual(expected_print, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_4_random_dice(self, mock_output):
        dice_list = [2, 3, 3, 6]
        print_dice(dice_list)
        expected_print = "Current dice:\nDie 1: 2\nDie 2: 3\nDie 3: 3\nDie 4: 6\n"
        self.assertEqual(expected_print, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_6_random_dice(self, mock_output):
        dice_list = [2, 3, 3, 6, 6, 6]
        print_dice(dice_list)
        expected_print = "Current dice:\nDie 1: 2\nDie 2: 3\nDie 3: 3\nDie 4: 6\nDie 5: 6\nDie 6: 6\n"
        self.assertEqual(expected_print, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_1_die(self, mock_output):
        dice_list = [6]
        print_dice(dice_list)
        expected_print = "Current dice:\nDie 1: 6\n"
        self.assertEqual(expected_print, mock_output.getvalue())
