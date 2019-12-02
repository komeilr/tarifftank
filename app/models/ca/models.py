from app.models import CABASE
from app.factory import db
import os

class CA2017(db.Model, CABASE):
  
    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"

class CA2018(CABASE):   

    cptpt = db.Column(db.String(), nullable=True)


class CA2019(db.Model, CABASE):   

    cptpt = db.Column(db.String(), nullable=True)
