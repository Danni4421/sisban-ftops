from sqlalchemy import Column, Integer, Float, CHAR
from ..database import db
from ..main.rules import RULES_SUMMARY

class Fuzzy(db.Model):
    __tablename__ = "fuzzy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    alternative = Column(CHAR(16))
    rule_index=Column(Integer)
    alpha_v1 = Column(Float)
    alpha_v2 = Column(Float)
    alpha = Column(Float)
    z_result = Column(Float)
    a_pred_multiply_z_pred = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'alternative': self.alternative,
            'rule_index': self.rule_index + 1,
            'alpha_v1': self.alpha_v1,
            'alpha_v2': self.alpha_v2,
            'alpha': self.alpha,
            'z_result': self.z_result,
            'a_pred_multiply_z_pred': self.a_pred_multiply_z_pred,
            'rule': RULES_SUMMARY[self.rule_index]
        }