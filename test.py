import unittest
import handler
class TestLetterService(unittest.TestCase):
    def test_all_letters_happy_path(self):
        input = "abcdefghijklmnopqrstuvwxyz"
        output = handler.contains_all_letters(input)
        self.assertEqual(True, output)
    def test_all_letters_with_spaces_happy_path(self):
        input = "abcdef ghijkl mn op qr stuvwxyz"
        output = handler.contains_all_letters(input)
        self.assertEqual(True, output)
    def test_all_letters_with_special_chars_happy_path(self):
        input = "abcdef? !ghijkl mn& $op* qr stuvwxyz"
        output = handler.contains_all_letters(input)
        self.assertEqual(True, output)
    def test_not_all_letters_with_chars(self):
        input = "abcdef? !ghijkl mn& $op* qr stuxyz"
        output = handler.contains_all_letters(input)
        self.assertEqual(False, output)
    def test_no_letters(self):
        input = ""
        output = handler.contains_all_letters(input)
        self.assertEqual(False, output)
    def test_not_all_letters_no_spaces(self):
        input = "abcdefghijklmnopqrstuvwxy"
        output = handler.contains_all_letters(input)
        self.assertEqual(True, output)