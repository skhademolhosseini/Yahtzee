from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import available_rows


class TestAvailableRows(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_available_rows_1_row(self, mock_output):
        score_sheet = {"Aces": 5, "Full House": -1}
        actual = available_rows(score_sheet)
        expected = ['2']
        expected_print = "Following rows are currently available in you score sheet.\n" \
                         "2: Full House\n"
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_output.getvalue())
