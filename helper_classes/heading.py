import app.ca.models


class HeadingCA:
    """class to hold all tariff classifications in a heading"""

    def __init__(self, heading, year='2019'):
        self.heading = self._validate_input(heading)
        self.year = self._validate_input(year)
        self.tariffs = self._query_tariffs()


    def _validate_input(self, _input):
        """validates input: heading/year"""

        if not isinstance(_input, str):
            raise TypeError("input must be str")
        elif len(_input) != 4:
            raise ValueError("input must be 4 digits")
        else:
            return _input

    
    def _format_hs(self, hscode: str) -> str:
        """input: 10 digit string representing HS code\nreturns string of length 13 with 3 dots added to HS code for better readability"""
        out = hscode[:4]

        return f"{hscode[:4]}.{hscode[4:6]}.{hscode[6:8]}.{hscode[8:]}"

    
    def _query_tariffs(self):
        """query's db for all tariff classifications of self.heading"""

        # determine which DB to query
        qryCLS = vars(app.ca.models)[f"CA{self.year}"]

        results = qryCLS.query.filter(qryCLS.tariff.like(f'{self.heading}%')).all()

        return results

    
    def _base_dict(self, tariffobj, level):
        """ returns basic dictionary structure for Heading type
        input: 3 element list containing hscode, description and unit of measure"""

        return {
            'tariff': tariffobj.tariff,
            'description': tariffobj.description,
            'uom': tariffobj.uom,
            'level': level
        }

    def _key_chain(self, tariff):
        """generates a list of strings signifying heading, subheading and tariff levels of a tariff
        input: str representing tariff gen_keychain('3926.90.99.90')
        \>>> ['3926', '3926.90', '3926.90.99']"""

        return [tariff[:i] for i in range(4, 9, 2)]


    def _get_dict_to_insert(self, hs_dict: dict, chain: list, level = 0) -> dict:
        """input: dictionary, list
        recursive, returns dictionary if key in chain"""

        if not chain:
            return hs_dict

        for _key in chain:
            if _key in hs_dict:
                hs_dict, level = self._get_dict_to_insert(hs_dict[_key], chain, level=level + 1)
                break
        return hs_dict, level
    
    
    def gen_tariff_dict(self):
        """generates dictionary structure of heading"""

        tariff_dict = {}
        level = 0
        heading = self.heading
        tariff_dict[heading] = self._base_dict(self.tariffs[0], level)
        ##print(f"DEBUG: {tariff_dict}")

        for tariffObj in self.tariffs[1:]:
            tariff = tariffObj.tariff
            curr_dict, level = self._get_dict_to_insert(tariff_dict, self._key_chain(tariff))
            curr_dict[tariff] = self._base_dict(tariffObj, level)

        return tariff_dict


    def book_view(self, _dict=None):
        d = _dict or self.gen_tariff_dict()
        for k, v in d.items():            
            if isinstance(v, dict):
                if len(k) % 2 != 0:
                    print("\t" * v['level'], v['description'])
                else:
                    print("\t" * v['level'], self._format_hs(k), "-" * v['level'], v['description'])
                self.book_view(v)


    def pdf_view(self, _dict=None):
        d = _dict or self.gen_tariff_dict()

        for k, v in d.items():
            if isinstance(v, dict):
                
