from sqlalchemy import Column, Integer, Float, ForeignKey
import enum
from ..database import db


class TopsisEuclideanDistance(db.Model):
    __tablename__ = "topsis_euclidean_distance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    alternative = Column(ForeignKey("topsis.id"))
    positive_distance = Column(Float)
    negative_distance = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'alternative': self.alternative,
            'positive_distance': self.positive_distance,
            'negative_distance': self.negative_distance
        }