"""
Testing submit_score from yahtzee.py
"""

from unittest import TestCase

from yahtzee import submit_lower_section_score


class TestLowerSectionSubmitScore(TestCase):

    def test_submit_lower_section_score_full_house_but_score_is_0(self):
        score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, 'Upper Score': 32, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 32}

        submit_lower_section_score(0, "12", score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, '\
Upper Score': 32, 'Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': 0, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 32}
        self.assertEqual(expected_new_score_sheet, score_sheet)

    def test_submit_lower_section_score_4_of_a_kind(self):
        score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, 'Upper Score': 32, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': 0, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 32}

        submit_lower_section_score(18, "11", score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, '\
Upper Score': 32, 'Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': 18, 'Full House': 0, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 18, 'Grand Total': 50}
        self.assertEqual(expected_new_score_sheet, score_sheet)

    def test_submit_lower_section_score_large_straight(self):
        score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, 'Upper Score': 32, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': 18, 'Full House': 0, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 18, 'Grand Total': 50}

        submit_lower_section_score(40, "14", score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, '\
Upper Score': 32, 'Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': 18, 'Full House': 0, '\
Small Straight': -1, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 58, 'Grand Total': 90}
        self.assertEqual(expected_new_score_sheet, score_sheet)
