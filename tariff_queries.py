import app.ca.models
from sqlalchemy import and_

class TariffRateCA:
    """ class used to obtain tariff rates and full stack description of 10-digit HS code"""

    def __init__(self, tariff, year='2019'):
        self.tariff = self._validate_tariff(tariff)
        self.year = self._validate_year(year)
        self.tobjs = self._get_rate_info()
        self.uom = self.tobjs[-1].uom
        self.ftas =  [
            'mfn', 'gt', 'aut', 'nzt', 'ccct', 'ldct', 
            'gpt', 'ust', 'mt', 'must', 'ciat', 'ct', 
            'crt', 'it', 'nt', 'slt', 'pt', 'colt', 
            'jt', 'pat', 'hnt', 'krt', 'ceut', 'uat', 'cptpt'
            ]
        self._process()


    def _validate_year(self, year):
        """validatees input: year"""

        if not isinstance(year, str):
            raise TypeError("input must be of type str")
        elif len(year) != 4:
            raise ValueError("input must be 4 chars in length")
        else:
            return year


    def _validate_tariff(self, tariff):
        """validates hs classification input"""

        if not isinstance(tariff, str):
            raise TypeError("input must be of type str")
        elif len(tariff) != 10:
            raise ValueError("input must be 10 chars in length")
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
                    queryClass.tariff.like(self.tariff[:i]),    # tariff = self.tariff
                    queryClass.description.isnot(None)          # description is not null
                    )).first()
            if q:
                results.append(q)

        return results


    def _process(self):
        """performs basic processing on tariff rates for easier access to data"""

        self.descriptions = {}
        self.rates = {}

        for tariff in self.tobjs:
            if tariff.description:
                self.descriptions[tariff.tariff] = tariff.description

            if tariff.mfn:
                for fta in self.ftas:
                    if hasattr(tariff, fta) and tariff.__getattribute__(fta):
                        self.rates[fta] = tariff.__getattribute__(fta)


    def __str__(self):
        out = ''

        for k, v in self.descriptions.items():
            out += f"{k}\t{v}\n"

        out += '\nFTA\tRATE\tUOM\n'
        for k, v in self.rates.items():
            out += f"{k}\t{v}\t{self.uom}\n"

        return out
                


def get_heading(heading, year='2019'):
    """returns list of sqlalchemy query objects pertaining to heading"""
    
    if len(heading) != 4 or not isinstance(heading, str):
        return
    
    queryClass = vars(app.ca.models)[f"CA{year}"]    

    results = queryClass.query.filter(queryClass.tariff.like(f'{heading}%')).all()  

    return results




