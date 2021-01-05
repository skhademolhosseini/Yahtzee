"""
Testing yahtzee_score_handler from yahtzee.py
"""

from unittest import TestCase

from yahtzee import yahtzee_score_handler


class TestYahtzeeScoreHandler(TestCase):

    def test_yahtzee_score_handler_not_a_yahtzee(self):
        dice_list = [1, 2, 2, 5, 6]
        score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Upper Score': 0, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': -1, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 0}

        yahtzee_score_handler(dice_list, score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '\
Upper Score': 0, 'Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 0, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 0}
        self.assertEqual(expected_new_score_sheet, score_sheet)

    def test_yahtzee_score_handler_the_first_yahtzee(self):
        dice_list = [2, 2, 2, 2, 2]
        score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Upper Score': 0, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': -1, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 0}

        yahtzee_score_handler(dice_list, score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '\
Upper Score': 0, 'Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 50, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 50, 'Grand Total': 50}
        self.assertEqual(expected_new_score_sheet, score_sheet)

    def test_yahtzee_score_handler_second_yahtzee(self):
        dice_list = [1, 1, 1, 1, 1]
        score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Upper Score': 0, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 50, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 50, 'Grand Total': 50}

        yahtzee_score_handler(dice_list, score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '\
Upper Score': 0, 'Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 50, 'Chance': -1, 'Yahtzee Bonus Count': 1, '\
Yahtzee Bonus Score': 100, 'Total Lower Score': 150, 'Grand Total': 150}
        self.assertEqual(expected_new_score_sheet, score_sheet)

    def test_yahtzee_score_handler_third_yahtzee(self):
        dice_list = [5, 5, 5, 5, 5]
        score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Upper Score': 0, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 50, 'Chance': -1, 'Yahtzee Bonus Count': 1, '\
Yahtzee Bonus Score': 100, 'Total Lower Score': 150, 'Grand Total': 150}

        yahtzee_score_handler(dice_list, score_sheet)

        expected_new_score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, '\
Upper Score': 0, 'Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': 50, 'Chance': -1, 'Yahtzee Bonus Count': 2, '\
Yahtzee Bonus Score': 200, 'Total Lower Score': 250, 'Grand Total': 250}
        self.assertEqual(expected_new_score_sheet, score_sheet)
