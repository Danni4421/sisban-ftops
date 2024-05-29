from sqlalchemy import Column, Integer, Float, Enum
import enum
from ..database import db


class BestWorstType(enum.Enum):
    BEST="best"
    WORST="worst"

class TopsisBestWorst(db.Model):
    __tablename__ = "topsis_best_worst"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Enum(BestWorstType), nullable=False)
    bw_kondisi_ekonomi = Column(Float)
    bw_tanggungan = Column(Float)
    bw_hutang = Column(Float)
    bw_aset = Column(Float)
    bw_biaya_listrik = Column(Float)
    bw_biaya_air = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'bw_kondisi_ekonomi': self.bw_kondisi_ekonomi,
            'bw_tanggungan': self.bw_tanggungan,
            'bw_hutang': self.bw_hutang,
            'bw_aset': self.bw_aset,
            'bw_biaya_listrik': self.bw_biaya_listrik,
            'bw_biaya_air': self.bw_biaya_air
        }