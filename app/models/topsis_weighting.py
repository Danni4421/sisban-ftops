from sqlalchemy import Column, Integer, Float, ForeignKey, CHAR
from ..database import db

class TopsisWeighting(db.Model):
    __tablename__ = "topsis_weighting"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bansos = Column(Integer, nullable=False)
    topsis_id = Column(ForeignKey("topsis.id"), nullable=False)
    alternative = Column(CHAR(16), nullable=False)
    weighted_kondisi_ekonomi = Column(Float)
    weighted_tanggungan = Column(Float)
    weighted_hutang = Column(Float)
    weighted_aset = Column(Float)
    weighted_biaya_listrik = Column(Float)
    weighted_biaya_air = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'topsis_id': self.topsis_id,
            'alternative': self.alternative,
            'weighted_kondisi_ekonomi': self.weighted_kondisi_ekonomi,
            'weighted_tanggungan': self.weighted_tanggungan,
            'weighted_hutang': self.weighted_hutang,
            'weighted_aset': self.weighted_aset,
            'weighted_biaya_listrik': self.weighted_biaya_listrik,
            'weighted_biaya_air': self.weighted_biaya_air
        }