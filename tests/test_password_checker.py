import unittest

from password_checker import PasswordStrengthChecker


class TestPasswordStrengthChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordStrengthChecker()

    def test_empty_password_is_weak_with_zero_entropy(self):
        result = self.checker.evaluate_strength("")
        self.assertEqual(result["entropy"], 0)
        self.assertEqual(result["strength"], "Weak")
        self.assertFalse(any(result["criteria"].values()))

    def test_strong_password_meets_all_criteria(self):
        result = self.checker.evaluate_strength("Test@123")
        self.assertTrue(all(result["criteria"].values()))
        self.assertEqual(result["strength"], "Strong")
        self.assertGreater(result["entropy"], 50)

    def test_short_password_fails_length(self):
        result = self.checker.evaluate_strength("Ab1!")
        self.assertFalse(result["criteria"]["length"])
        # Other character classes still count toward the score.
        self.assertEqual(result["strength"], "Moderate")

    def test_moderate_password_partial_criteria(self):
        result = self.checker.evaluate_strength("password1")
        self.assertTrue(result["criteria"]["length"])
        self.assertTrue(result["criteria"]["lowercase"])
        self.assertTrue(result["criteria"]["digit"])
        self.assertEqual(result["strength"], "Moderate")


if __name__ == "__main__":
    unittest.main()
