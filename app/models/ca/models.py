from app.models import CABASE
import os

class CA2017(CABASE):
  

    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"

class CA2018(CABASE):   

    cptpt = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"

class CA2019(CABASE):   

    cptpt = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"