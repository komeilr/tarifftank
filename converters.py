import json
import csv


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


def to_csv(data, filename, path='.'):
    with open(f"{path}/{filename}.csv", 'w') as f:

        writer = csv.writer(f, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

        for row in data:
            if isinstance(row, list):
                writer.writerow(row)
            elif isinstance(row, dict):
                # write headers once
                if data.index(row) == 0:
                    writer.writerow(row.keys())
                writer.writerow(row.values())
        
        return True


