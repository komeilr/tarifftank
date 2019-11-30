from .cabase import CABASE
import os

class CA2017(CABASE):
  

    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"