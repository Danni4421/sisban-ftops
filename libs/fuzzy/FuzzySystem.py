from .FuzzyRule import FuzzyRule
from typing import Tuple


class Fuzzy:
    rules: Tuple[FuzzyRule, ...]

    def __init__(self, rules, data):
        self.rules = rules
        self.data = data

    def exec(self):
        result = []
        alpha_s = []

        for rule in self.rules:
            alpha_predicate_multiply_z, alpha = rule.calculate_reward(data=self.data)
            result.append(alpha_predicate_multiply_z)
            alpha_s.append(alpha)

        return sum(result) / sum(alpha_s)
