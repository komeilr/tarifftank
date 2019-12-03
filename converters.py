import json


def json_to_str(filename):
    """ imports json file as string """

    json_data = None
    with open(f"app/data/ca/{filename}.json", 'r') as f:
        json_data = f.read()
    return json_data

def json_to_obj(json_str):
    """converts json string to dictionary"""

    try:
        d = json.loads(json_str)
        return d
        
    except TypeError as e:
        print(e)
