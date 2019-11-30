from app.factory import db
import os

class CABASE(db.Model):
    __tablename__ = "ca2017"
    id = db.Column(db.Integer, primary_key=True)
    tariff = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    uom = db.Column(db.String(255), nullable=True)
    mfn = db.Column(db.String(), nullable=True)
    gt = db.Column(db.String(), nullable=True)
    aut = db.Column(db.String(), nullable=True)
    nzt = db.Column(db.String(), nullable=True)
    ccct = db.Column(db.String(), nullable=True)
    ldct = db.Column(db.String(), nullable=True)
    gpt = db.Column(db.String(), nullable=True)
    ust = db.Column(db.String(), nullable=True)
    mt = db.Column(db.String(), nullable=True)
    must = db.Column(db.String(), nullable=True)
    ciat = db.Column(db.String(), nullable=True)
    ct = db.Column(db.String(), nullable=True)
    crt = db.Column(db.String(), nullable=True)
    it = db.Column(db.String(), nullable=True)
    nt = db.Column(db.String(), nullable=True)
    slt = db.Column(db.String(), nullable=True)
    pt = db.Column(db.String(), nullable=True)
    colt = db.Column(db.String(), nullable=True)
    jt = db.Column(db.String(), nullable=True)
    pat = db.Column(db.String(), nullable=True)
    hnt = db.Column(db.String(), nullable=True)
    krt = db.Column(db.String(), nullable=True)
    ceut = db.Column(db.String(), nullable=True)
    uat = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f"<{self.__tablename__} {self.tariff}>"

    def __str__(self):
        return f"<{self.__tablename__} {self.tariff}>"