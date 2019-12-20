import requests
from bs4 import BeautifulSoup
import csv


pgapage = {
    'cfia': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/cfia-acia-eng.html',
    'cnsc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/cnsc-ccsn-eng.html',
    'eccc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/eccc-eccc-eng.html',
    'dfo': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/dfo-mpo-eng.html',
    'gac': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/gac-amc-eng.html',
    'hc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/hc-sc-eng.html',
    'nrcan': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/nrc-rnc-eng.html',
    'phac': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/phac-aspc-eng.html',
    'tc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/tc-eng.html'
}


def get_table_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []

    table = soup.find(class_='brdr-bttm')

    # headers
    table_head = table.find('thead')

    rows = table_head.find_all('tr')
    for row in rows:
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

    # body
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')       
        cols = [ele.text.strip() for ele in cols]       
        data.append([ele for ele in cols])

    return data

def get_logic_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []

    table = soup.find(class_='table-bordered')

    # headers
    table_head = table.find('thead')

    rows = table_head.find_all('tr')
    for row in rows:
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

    # body
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')       
        cols = [ele.text.strip() for ele in cols]       
        data.append([ele for ele in cols])
    return data

def data_to_csv(pga, dtype='data'):

    # open csv file
    if dtype == 'data':
        data = get_table_data(pga)
    elif dtype == 'logic':
        data = get_logic_data(pga)
    else:
        raise ValueError("dtype must be 'logic' or 'data'")

    with open(f'app/data/ca/{pga}_PGA_{'logic' if dtype.lower() == 'logic', else 'DATA'}', 'w') as f:

        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        #data = get_table_data(pgapage[pga])

        for line in data:
            writer.writerow(line)


if __name__=='__main__':
    for pga in pgapage:
        data_to_csv(pga, 'logic')