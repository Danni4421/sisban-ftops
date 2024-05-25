from typing import Dict, TypedDict
from .FuzzyMember import FuzzyMember, MemberReward


class Membership(TypedDict):
    member_name: str
    member: FuzzyMember | MemberReward


class FuzzyRule:
    antecedent: Dict[Membership, ...]
    consequent: Membership

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def calculate_reward(self, data):
        alpha_s = []
        data_keys = list(data.keys())

        for idx in range(len(data_keys)):
            antecedent = self.antecedent.get(data_keys[idx])
            alpha = antecedent.get('member').fuzzify(x=data.get(data_keys[idx]))
            alpha_s.append(alpha)

        min_value = min(alpha_s)
        return self.consequent.get('member').get_reward(alpha=min_value) * min_value, min_value
