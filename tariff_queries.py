import app.ca.models              


def get_heading(heading, year='2019'):
    """returns list of sqlalchemy query objects pertaining to heading"""
    
    if len(heading) != 4 or not isinstance(heading, str):
        return
    
    queryClass = vars(app.ca.models)[f"CA{year}"]    

    results = queryClass.query.filter(queryClass.tariff.like(f'{heading}%')).all()  

    return results




