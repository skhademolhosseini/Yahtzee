from unittest import TestCase

from yahtzee import submit_upper_section_score


class TestSubmitUpperSection(TestCase):

    def test_submit_upper_section_score_Aces_but_score_is_0(self):
        score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, 'Upper Score': 32, '\
Upper Bonus': 0, 'Total Upper Score': 32, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 32}

        submit_upper_section_score(0, "1", score_sheet)

        expected_new_score_sheet = {'Aces': 0, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, '\
Upper Score': 32, 'Upper Bonus': 0, 'Total Upper Score': 32, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 32}
        self.assertEqual(expected_new_score_sheet, score_sheet)

    def test_submit_upper_section_score_threes_kind(self):
        score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': 24, 'Upper Score': 32, '\
Upper Bonus': 0, 'Total Upper Score': 32, '3 of a kind': -1, '4 of a kind': -1, 'Full House': 0, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 32}

        submit_upper_section_score(9, "3", score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': 8, 'Threes': 9, 'Fours': -1, 'Fives': -1, 'Sixes': 24, '\
Upper Score': 41, 'Upper Bonus': 0, 'Total Upper Score': 41, '3 of a kind': -1, '4 of a kind': -1, 'Full House': 0, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 41}
        self.assertEqual(expected_new_score_sheet, score_sheet)

