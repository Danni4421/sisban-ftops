from sqlalchemy import Column, Integer, Float, ForeignKey, CHAR
from ..database import db

class TopsisNormalization(db.Model):
    __tablename__ = "topsis_normalization"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bansos = Column(Integer, nullable=False)
    topsis_id = Column(ForeignKey("topsis.id"), nullable=False)
    alternative = Column(CHAR(16), nullable=False)
    normalize_kondisi_ekonomi = Column(Float)
    normalize_tanggungan = Column(Float)
    normalize_hutang = Column(Float)
    normalize_aset = Column(Float)
    normalize_biaya_listrik = Column(Float)
    normalize_biaya_air = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'topsis_id': self.topsis_id,
            'alternative': self.alternative,
            'normalize_kondisi_ekonomi': self.normalize_kondisi_ekonomi,
            'normalize_tanggungan': self.normalize_tanggungan,
            'normalize_hutang': self.normalize_hutang,
            'normalize_aset': self.normalize_aset,
            'normalize_biaya_listrik': self.normalize_biaya_listrik,
            'normalize_biaya_air': self.normalize_biaya_air
        }