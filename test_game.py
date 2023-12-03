"""
Template to test game functions
"""
import unittest
from run import choose_word, WORD_LIST, dashed_word_rep, wtw
from unittest.mock import patch

class TestGameFunctions(unittest.TestCase):
    """
    Test if chosen word is in the list
    """
    def test_choose_word(self):
        "Test if chosen word is word from the list"
        chosen_word = choose_word()
        self.assertIn(chosen_word, WORD_LIST)

    def test_dashed_word_rep(self):
        "Test dashed_word_rep with inputs"
        word = 'BART'
        guessed_letters = ['R', 'T']
        result = dashed_word_rep(word, guessed_letters)
        self.assertEqual(result, "_ _ R T")

    @patch('builtins.print')
    def test_wtw(self, mock_print):
        "Test that the print function is called 3 times when wtw is executed"
        wtw()
        self.assertEqual(mock_print.call_count, 3)

if __name__ == '__main__':
    unittest.main()
