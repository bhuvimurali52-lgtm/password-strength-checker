import re
import math

class PasswordStrengthChecker:
    def __init__(self):
        self.patterns = {
            "length": r".{8,}",
            "uppercase": r"[A-Z]",
            "lowercase": r"[a-z]",
            "digit": r"\d",
            "special": r"[!@#$%^&*(),.?\":{}|<>]"
        }

    def check_criteria(self, password):
        results = {}
        for key, pattern in self.patterns.items():
            results[key] = bool(re.search(pattern, password))
        return results

    def calculate_entropy(self, password):
        charset_size = 0

        if re.search(r"[a-z]", password):
            charset_size += 26
        if re.search(r"[A-Z]", password):
            charset_size += 26
        if re.search(r"\d", password):
            charset_size += 10
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            charset_size += 32

        if charset_size == 0:
            return 0

        entropy = len(password) * math.log2(charset_size)
        return round(entropy, 2)

    def evaluate_strength(self, password):
        criteria = self.check_criteria(password)
        entropy = self.calculate_entropy(password)

        score = sum(criteria.values())

        if score <= 2:
            strength = "Weak"
        elif score == 3 or score == 4:
            strength = "Moderate"
        else:
            strength = "Strong"

        return {
            "criteria": criteria,
            "entropy": entropy,
            "strength": strength
        }


# 🔄 Real-time style usage (CLI simulation)
if __name__ == "__main__":
    checker = PasswordStrengthChecker()

    while True:
        password = input("\nEnter password (or 'exit'): ")
        if password.lower() == "exit":
            break

        result = checker.evaluate_strength(password)

        print("\n--- Analysis ---")
        for k, v in result["criteria"].items():
            print(f"{k.capitalize():<10}: {'✔' if v else '✘'}")

        print(f"Entropy   : {result['entropy']} bits")
        print(f"Strength  : {result['strength']}")
