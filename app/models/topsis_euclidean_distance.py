from sqlalchemy import Column, Integer, Float, ForeignKey, CHAR
import enum
from ..database import db


class TopsisEuclideanDistance(db.Model):
    __tablename__ = "topsis_euclidean_distance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    topsis_id = Column(ForeignKey("topsis.id"), nullable=False)
    alternative = Column(CHAR(16), nullable=False)
    bansos = Column(Integer, nullable=True)
    positive_distance = Column(Float)
    negative_distance = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'topsis_id': self.topsis_id,
            'alternative': self.alternative,
            'positive_distance': self.positive_distance,
            'negative_distance': self.negative_distance
        }