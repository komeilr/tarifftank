from app.factory import db


class Base_Mixin():

    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"

    def __str__(self):
        return f"<{self.__tablename__} {self.tariff}>"



class CA2017(db.Model):
    __tablename__="ca2017"

    id = db.Column(db.Integer, primary_key=True)
    tariff = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    uom = db.Column(db.String(255), nullable=True)
    mfn = db.Column(db.String(255), nullable=True)
    gt = db.Column(db.String(255), nullable=True)
    aut = db.Column(db.String(255), nullable=True)
    nzt = db.Column(db.String(255), nullable=True)
    ccct = db.Column(db.String(255), nullable=True)
    ldct = db.Column(db.String(255), nullable=True)
    gpt = db.Column(db.String(255), nullable=True)
    ust = db.Column(db.String(255), nullable=True)
    mt = db.Column(db.String(255), nullable=True)
    must = db.Column(db.String(255), nullable=True)
    ciat = db.Column(db.String(255), nullable=True)
    ct = db.Column(db.String(255), nullable=True)
    crt = db.Column(db.String(255), nullable=True)
    it = db.Column(db.String(255), nullable=True)
    nt = db.Column(db.String(255), nullable=True)
    slt = db.Column(db.String(255), nullable=True)
    pt = db.Column(db.String(255), nullable=True)
    colt = db.Column(db.String(255), nullable=True)
    jt = db.Column(db.String(255), nullable=True)
    pat = db.Column(db.String(255), nullable=True)
    hnt = db.Column(db.String(255), nullable=True)
    krt = db.Column(db.String(255), nullable=True)
    ceut = db.Column(db.String(255), nullable=True)
    uat = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"

    def __str__(self):
        return f"<{self.__tablename__} {self.tariff}>"
  

class CA2018(db.Model, Base_Mixin):
    __tablename__ = "ca2018"

    id = db.Column(db.Integer, primary_key=True)
    tariff = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    uom = db.Column(db.String(255), nullable=True)
    mfn = db.Column(db.String(255), nullable=True)
    gt = db.Column(db.String(255), nullable=True)
    aut = db.Column(db.String(255), nullable=True)
    nzt = db.Column(db.String(255), nullable=True)
    ccct = db.Column(db.String(255), nullable=True)
    ldct = db.Column(db.String(255), nullable=True)
    gpt = db.Column(db.String(255), nullable=True)
    ust = db.Column(db.String(255), nullable=True)
    mt = db.Column(db.String(255), nullable=True)
    must = db.Column(db.String(255), nullable=True)
    ciat = db.Column(db.String(255), nullable=True)
    ct = db.Column(db.String(255), nullable=True)
    crt = db.Column(db.String(255), nullable=True)
    it = db.Column(db.String(255), nullable=True)
    nt = db.Column(db.String(255), nullable=True)
    slt = db.Column(db.String(255), nullable=True)
    pt = db.Column(db.String(255), nullable=True)
    colt = db.Column(db.String(255), nullable=True)
    jt = db.Column(db.String(255), nullable=True)
    pat = db.Column(db.String(255), nullable=True)
    hnt = db.Column(db.String(255), nullable=True)
    krt = db.Column(db.String(255), nullable=True)
    ceut = db.Column(db.String(255), nullable=True)
    uat = db.Column(db.String(255), nullable=True)
    cptpt = db.Column(db.String(255), nullable=True)


class CA2019(db.Model, Base_Mixin):   

    __tablename__ = "ca2019"

    id = db.Column(db.Integer, primary_key=True)
    tariff = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    uom = db.Column(db.String(255), nullable=True)
    mfn = db.Column(db.String(255), nullable=True)
    gt = db.Column(db.String(255), nullable=True)
    aut = db.Column(db.String(255), nullable=True)
    nzt = db.Column(db.String(255), nullable=True)
    ccct = db.Column(db.String(255), nullable=True)
    ldct = db.Column(db.String(255), nullable=True)
    gpt = db.Column(db.String(255), nullable=True)
    ust = db.Column(db.String(255), nullable=True)
    mt = db.Column(db.String(255), nullable=True)
    must = db.Column(db.String(255), nullable=True)
    ciat = db.Column(db.String(255), nullable=True)
    ct = db.Column(db.String(255), nullable=True)
    crt = db.Column(db.String(255), nullable=True)
    it = db.Column(db.String(255), nullable=True)
    nt = db.Column(db.String(255), nullable=True)
    slt = db.Column(db.String(255), nullable=True)
    pt = db.Column(db.String(255), nullable=True)
    colt = db.Column(db.String(255), nullable=True)
    jt = db.Column(db.String(255), nullable=True)
    pat = db.Column(db.String(255), nullable=True)
    hnt = db.Column(db.String(255), nullable=True)
    krt = db.Column(db.String(255), nullable=True)
    ceut = db.Column(db.String(255), nullable=True)
    uat = db.Column(db.String(255), nullable=True)
    cptpt = db.Column(db.String(255), nullable=True)