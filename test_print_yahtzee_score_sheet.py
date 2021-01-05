"""
Testing print_yahtzee_score_sheet from yahtzee.py
"""

from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import print_yahtzee_score_sheet


class TestPrintYahtzeeScoreSheet(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_yahtzee_score_sheet_starting_score_sheet(self, mock_output):
        score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Upper Score': 0, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': -1, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 0}
        print_yahtzee_score_sheet(score_sheet)
        expected_print = "Current state of your score sheet (not used rows are displayed as -1):\n" \
                         "1. Aces: -1\n" \
                         "2. Twos: -1\n" \
                         "3. Threes: -1\n" \
                         "4. Fours: -1\n" \
                         "5. Fives: -1\n" \
                         "6. Sixes: -1\n" \
                         "7. Upper Score: 0\n" \
                         "8. Upper Bonus: 0\n" \
                         "9. Total Upper Score: 0\n" \
                         "10. 3 of a kind: -1\n" \
                         "11. 4 of a kind: -1\n" \
                         "12. Full House: -1\n" \
                         "13. Small Straight: -1\n" \
                         "14. Large Straight: -1\n" \
                         "15. YAHTZEE: -1\n" \
                         "16. Chance: -1\n" \
                         "17. Yahtzee Bonus Count: 0\n" \
                         "18. Yahtzee Bonus Score: 0\n" \
                         "19. Total Lower Score: 0\n" \
                         "20. Grand Total: 0\n"
        self.assertEqual(expected_print, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_yahtzee_score_sheet_some_rows_filled(self, mock_output):
        score_sheet = {'Aces': 3, 'Twos': 6, 'Threes': -1, 'Fours': 4, 'Fives': -1, 'Sixes': 18, 'Upper Score': 31, '\
Upper Bonus': 0, 'Total Upper Score': 31, '3 of a kind': -1, '4 of a kind': -1, 'Full House': 25, '\
Small Straight': -1, 'Large Straight': 40, 'YAHTZEE': 50, 'Chance': -1, 'Yahtzee Bonus Count': 1, '\
Yahtzee Bonus Score': 100, 'Total Lower Score': 215, 'Grand Total': 246}
        print_yahtzee_score_sheet(score_sheet)
        expected_print = "Current state of your score sheet (not used rows are displayed as -1):\n" \
                         "1. Aces: 3\n" \
                         "2. Twos: 6\n" \
                         "3. Threes: -1\n" \
                         "4. Fours: 4\n" \
                         "5. Fives: -1\n" \
                         "6. Sixes: 18\n" \
                         "7. Upper Score: 31\n" \
                         "8. Upper Bonus: 0\n" \
                         "9. Total Upper Score: 31\n" \
                         "10. 3 of a kind: -1\n" \
                         "11. 4 of a kind: -1\n" \
                         "12. Full House: 25\n" \
                         "13. Small Straight: -1\n" \
                         "14. Large Straight: 40\n" \
                         "15. YAHTZEE: 50\n" \
                         "16. Chance: -1\n" \
                         "17. Yahtzee Bonus Count: 1\n" \
                         "18. Yahtzee Bonus Score: 100\n" \
                         "19. Total Lower Score: 215\n" \
                         "20. Grand Total: 246\n"
        self.assertEqual(expected_print, mock_output.getvalue())
