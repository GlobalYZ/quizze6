from unittest import TestCase

from exceptions_quiz import check_password_strength


class Test(TestCase):
    def test_strong_password(self):
        self.assertEqual(True, check_password_strength("UPPERlower123"))

    def test_less_than_eight_chars(self):
        with self.assertRaises(ValueError):
            check_password_strength("1Lo")

    def test_no_upper_case(self):
        with self.assertRaises(ValueError):
            check_password_strength("asjdfjk3")

    def test_no_lower_case(self):
        with self.assertRaises(ValueError):
            check_password_strength("ANDJEUL9")

    def test_no_digits(self):
        with self.assertRaises(ValueError):
            check_password_strength("HelloTHERE")
