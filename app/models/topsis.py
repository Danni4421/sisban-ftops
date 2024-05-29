from sqlalchemy import Column, Integer, Float, CHAR
from ..database import db

class Topsis(db.Model):
    __tablename__ = "topsis"

    id = Column(CHAR(16), primary_key=True)
    kondisi_ekonomi = Column(Float)
    tanggungan = Column(Integer)
    hutang = Column(Float)
    aset = Column(Float)
    biaya_listrik = Column(Float)
    biaya_air = Column(Float)
    preference_value = Column(Float)
    rank = Column(Integer)

    def to_dict(self):
        return {
            'alternative': self.id,
            'kondisi_ekonomi': self.kondisi_ekonomi,
            'tanggungan': self.tanggungan,
            'hutang': self.hutang,
            'aset': self.aset,
            'biaya_listrik': self.biaya_listrik,
            'biaya_air': self.biaya_air,
            'preference_value': self.preference_value,
            'rank': self.rank
        }