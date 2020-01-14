import copy

import app.ca.models



class HeadingCA:
    """class to hold all tariff classifications in a heading"""

    def __init__(self, heading, year='2020'):
        self.heading = self._validate_input(heading)
        self.year = self._validate_input(year)
        self.tariffs = self._query_tariffs()
        self.description = self.tariffs[0].description
        self.chapter_notes = self._query_chapter_notes()
        self.section_notes = self.chapter_notes.section


    def _query_chapter_notes(self):
        query = app.ca.models.Chapter.query.filter_by(chapter=self.heading[:2]).first()
        return query


    def _validate_input(self, _input):
        """validates input: heading/year"""

        if not isinstance(_input, str):
            raise TypeError("input must be str")
        elif len(_input) not in  [4, 6]:
            raise ValueError("input must be 4 digits")
        else:
            return _input

    def _format_hs(self, hscode: str) -> str:
        """input: 10 digit string representing HS code\nreturns string of length 13 with 3 dots added to HS code for better readability"""
        out = hscode[:4]

        if len(hscode) == 4:
            return f"{hscode[:2]}.{hscode[2:]}"

        if len(hscode) == 6:
            return f"{hscode[:4]}.{hscode[4:]}"

        if len(hscode) == 8:
            return f"{hscode[:4]}.{hscode[4:6]}.{hscode[6:]}"

        if len(hscode) == 10:
            return f"{hscode[:4]}.{hscode[4:6]}.{hscode[6:8]}.{hscode[8:]}"
       
    
    def _query_tariffs(self):
        """query's db for all tariff classifications of self.heading"""

        # determine which DB to query
        qryCLS = vars(app.ca.models)[f"CA{self.year}"]

        results = qryCLS.query.filter(qryCLS.tariff.like(f'{self.heading}%')).all()
        if not results:
            raise ValueError(f"Heading {self.heading} doesn't exit")

        return results

    
    def _base_dict(self, tariffobj, level):
        """ returns basic dictionary structure for Heading type
        input: 3 element list containing hscode, description and unit of measure"""


        return {
            'tariff': tariffobj.tariff,
            'formatted_hs': self._format_hs(tariffobj.tariff),
            'description': tariffobj.description,
            'is_heading':level < 1,
            'year':self.year,
            'uom': tariffobj.uom,
            'level': level,
            'is_link':len(tariffobj.tariff) == 10,
            'is_general_description':len(tariffobj.tariff) in [5, 7, 9],
            'dashes':self._get_dashes(tariffobj.tariff)
        }

    
    def _get_dashes(self, tariff):
        return len(tariff[4:]) - min(1, tariff[-2:].count('0'))





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


    def book_view_terminal(self, _dict=None):
        """ prints to terminal book view format of heading recursively"""
        d = _dict or self.gen_tariff_dict()
        for k, v in d.items():            
            if isinstance(v, dict):
                if len(k) % 2 != 0:
                    print("\t" * v['level'] + "-" * (len(k) - 5) + f" {v['description']}")
                else:
                    print("\t" * v['level'], self._format_hs(k), "-" * (len(k) - 5), v['description'])
                self.book_view_terminal(v)


    def book_view_web(self):
        out = []
        duty_rate_8 = None
        for t in self.tariffs:            
            d = {'tariff':'', 'ss':'', 'dashes':1, 'description':'', 'uom':'', 'mfn':'', 'apt':{}}

            if t.tariff:
                if len(t.tariff) % 2 == 1:
                    d['tariff'] = ''
                    
                elif len(t.tariff) == 10:                    
                    d['tariff'] = t.tariff[:8]
                    d['ss'] = t.tariff[-2:]

                elif len(t.tariff) == 8:
                    duty_rate_8 = copy.deepcopy(t)
                    #print(duty_rate_8)
                    d['tariff'] = ''
                else:
                    d['tariff'] = t.tariff[:8]

            d['dashes'] = self._get_dashes(t.tariff)             
            
            if t.description:
                #print(t.description)
                d['description'] = t.description
            
            if t.uom:
                d['uom'] = t.uom

            t_to_check = t
            if len(t.tariff) == 10:
                if not t.mfn:
                    d['mfn'] = duty_rate_8.mfn
                    t_to_check = duty_rate_8                    
            
                else:
                    d['mfn'] = t.mfn
                    duty_rate_8 = None

                for fta in ['gt', 'aut', 'nzt', 'ccct', 'ldct', 'gpt', 'ust', 'mt', 'must', 'ciat', 'ct', 
                            'crt', 'it', 'nt', 'slt', 'pt', 'colt', 'jt', 'pat', 'hnt', 'krt', 'ceut', 'uat', 
                            'cptpt']:
                    
                    if hasattr(t_to_check, fta) and t_to_check.__getattribute__(fta):
                        tariff_fta = t_to_check.__getattribute__(fta)

                        if tariff_fta in d['apt']:
                            d['apt'][tariff_fta].append(fta)
                        else:
                            d['apt'][tariff_fta] = [fta]
            
            out.append(d)

        return out                  

