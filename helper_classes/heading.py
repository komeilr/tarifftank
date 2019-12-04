import app.ca.models

class HeadingCA:
    """class to hold all tariff classifications in a heading"""
    def __init__(self, heading, year='2019'):
        self.heading = self._validate_heading(heading)
        self.year = self._validate_year(year)
        self.tariffs = self._query_tariffs()


    def _validate_year(self, year):
        """validate input: year"""
        if not isinstance(year, str):
            raise TypeError("input must be str")
        elif len(year) != 4:
            raise ValueError("input must be 4 digits")
        else:
            return year

    def _validate_heading(self, heading):
        """validates input: heading"""

        if not isinstance(heading, str):
            raise TypeError("input must be str")
        elif len(heading) != 4:
            raise ValueError("input must be 4 digits")
        else:
            return heading

    
    def _query_tariffs(self):
        """query's db for all tariff classifications of self.heading"""

        # determine which DB to query
        qryCLS = vars(app.ca.models)[f"CA{self.year}"]

        results = qryCLS.query.filter(qryCLS.tariff.like(f'{self.heading}%')).all()

        return results