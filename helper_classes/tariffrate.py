import app.ca.models
from sqlalchemy import and_


FTAS =  [
    'mfn', 'gt', 'aut', 'nzt', 'ccct', 'ldct', 'gpt', 'ust', 'mt', 'must', 'ciat', 'ct', 
    'crt', 'it', 'nt', 'slt', 'pt', 'colt', 'jt', 'pat', 'hnt', 'krt', 'ceut', 'uat', 'cptpt'
]

class TariffRateCA:
    """ class used to obtain tariff rates and full stack description of 10-digit HS code"""

    def __init__(self, tariff, year='2020'):
        self.year = year
        self.tariff = self._validate_tariff(tariff)        
        self.tobjs = self._get_rate_info()
        self.uom = self.tobjs[-1].uom
        self.descriptions = {}
        self.rates = {}
        self.pgas = []
        self.chapter_notes = self._query_chapter_notes()
        self.section_notes = self.chapter_notes.section
        
        # processes query and populates attributes
        self._process()

    
    def _get_pgas(self):
        #TODO: write pga query code
        # query for pga and append list to self.pgas
        pass


    def _query_chapter_notes(self):

        query = app.ca.models.Chapter.query.filter_by(chapter=self.tariff[:2]).first()
        return query


    def _validate_tariff(self, tariff):
        """validates hs classification input"""

        if not vars(app.ca.models)[f"CA{self.year}"].query.filter_by(tariff=tariff).first():
            raise ValueError("invalid tariff code")
        else:
            return tariff


    def _get_rate_info(self):
        """queries db"""

        # determine table to query
        queryClass = vars(app.ca.models)[f"CA{self.year}"]
    
        results = []
        for i in range(4, 11):
            q = queryClass.query.filter(
                and_(
                    queryClass.tariff.like(self.tariff[:i]),    # tariff = self.tariff from 4 digits to all 10
                    queryClass.description.isnot(None)          # description is not null
                    )).first()
            if q:
                results.append(q)
        return results


    def _process(self):
        """performs basic processing on tariff rates for easier access to data"""
        
        for tariff in self.tobjs:
            if tariff.description:
                self.descriptions[tariff.tariff] = tariff.description

            if tariff.mfn:
                for fta in FTAS:
                    if hasattr(tariff, fta) and tariff.__getattribute__(fta):
                        self.rates[fta] = tariff.__getattribute__(fta)

        self._get_pgas()
    
    def __str__(self):
        out = ''

        for k, v in self.descriptions.items():
            out += f"{k}\t{v}\n"

        out += '\nFTA\tRATE\tUOM\n'
        for k, v in self.rates.items():
            out += f"{k}\t{v}\t{self.uom}\n"

        return out