from .FuzzyRule import FuzzyRule
from typing import Tuple


class Fuzzy:
    rules: Tuple[FuzzyRule, ...]
    total_alpha_pred: int
    total_a_pred_multiply_z_pred: int

    def __init__(self, rules, data):
        self.rules = rules
        self.data = data
        self.total_alpha_pred = 0
        self.total_a_pred_multiply_z_pred = 0

    def exec(self):
        res_data = []

        for rule in self.rules:
            res = rule.calculate_reward(data=self.data)
            res_data.append(res)
            self.total_alpha_pred += res.get('alpha_pred')
            self.total_a_pred_multiply_z_pred += res.get('a_pred_multiply_z_pred')

        return (self.total_a_pred_multiply_z_pred / self.total_alpha_pred, res_data)
