from typing import Dict, TypedDict, Any
from .FuzzyMember import FuzzyMember, MemberReward


class Membership(TypedDict):
    member_name: str
    member: FuzzyMember | MemberReward


class FuzzyRule:
    antecedent: Dict[Membership, Any]
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

        alpha = min(alpha_s)
        z_pred = self.consequent.get('member').get_reward(alpha)
        a_pred_multiply_z_pred = z_pred * alpha
        
        return {
            'alpha_s': alpha_s,
            'alpha_pred': alpha,
            'z_pred': z_pred,
            'a_pred_multiply_z_pred': a_pred_multiply_z_pred
        }
