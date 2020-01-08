import json
import csv
import os


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

def csv_to_json(filename, path='./'):
    data = []
    out = []
    try:
        with open(f'{path}{filename}.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')

            for line in reader:
                data.append(line)

        keys = data[0]
        rows = data[1:]

        for line in rows:
            l = line[:]
            l[0] = l[0].replace('.', '')
            out.append({k:v for k, v in zip(keys, l)})

        with open(f'{path}{filename}.json', 'w') as f:
            json.dump(out, f)

    except Exception as e:
        print(e)


