import app.ca.models

class TariffRateCA:
    def __init__(self, tariff, year='2019'):
        self.tariff = tariff
        self.year = year
        self.tobjs = self.get_rate_info()
        self.ftas =  [
            'mfn', 'gt', 'aut', 'nzt', 'ccct', 'ldct', 
            'gpt', 'ust', 'mt', 'must', 'ciat', 'ct', 
            'crt', 'it', 'nt', 'slt', 'pt', 'colt', 
            'jt', 'pat', 'hnt', 'krt', 'ceut', 'uat', 'cptpt'
            ]

    def get_rate_info(self):
        queryClass = vars(app.ca.models)[f"CA{self.year}"]
    
        results = []
        for i in range(4, 11):
            q = queryClass.query.filter_by(tariff=self.tariff[:i]).first()
            if q:
                results.append(q)

        return results

    def __str__(self):
        out_description = ""

        out_rates = "\nFTA\tRATE\tUOM\n"

        for tariff in self.tobjs:
            if tariff.description:
                out_description += f"{tariff.tariff} {tariff.description}"
                out_description += "\n"

            if tariff.uom:
                for fta in self.ftas:
                    out_rates += f"{fta}\t{tariff.__getattribute__(fta)}\t{tariff.uom}\n"

        return out_description + out_rates
                


def get_ca_rate_info(tariff, year='2019'):
    """returns list of sqlalchemy query objects pertaining to the tariff"""
    
    queryClass = vars(app.ca.models)[f"CA{year}"]
    
    results = []
    for i in range(4, 11):
        q = queryClass.query.filter_by(tariff=tariff[:i]).first()
        if q:
            results.append(q)

    return results


def get_heading(heading, year='2019'):
    """returns list of sqlalchemy query objects pertaining to heading"""
    
    if len(heading) != 4 or not isinstance(heading, str):
        return
    
    queryClass = vars(app.ca.models)[f"CA{year}"]    

    results = queryClass.query.filter(queryClass.tariff.like(f'{heading}%')).all()  

    return results




