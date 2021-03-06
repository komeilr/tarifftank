import csv
import json
import os

from flask import (
    Blueprint, 
    render_template, 
    redirect, 
    url_for, 
    flash, 
    session
)

from helper_classes.heading import HeadingCA
from helper_classes.tariffrate import TariffRateCA
import app.ca.models

ca_bp = Blueprint('ca', __name__, url_prefix='/ca/', template_folder='templates')


# ----------HEADING-------------
@ca_bp.route('/<year>/heading/<tariff>')
def heading_lookup(year, tariff):

    if len(tariff) in [4, 6]:
        try:
            if session['year']:
                h = HeadingCA(tariff, session['year'])
            else:
                h = HeadingCA(tariff, year)
      
            return render_template('ca/heading-lookup.html', title=f"Heading {tariff}", year=year, h=h)
        except Exception as e:            
            flash(f"Invalid heading {tariff}, {e}")
    else:
        flash(f"Invalid tariff {tariff}")
    return redirect(url_for('main.index'))

# ----------10 DIGIT HS-------------
@ca_bp.route('/<year>/tariff/<tariff>')
def tariff_lookup(year, tariff):

    if len(tariff) == 10:
        try:
            dev = ''
            if os.environ.get('FLASK_ENV') == 'development':
                dev = '/kras'
            if session['year']:
                t = TariffRateCA(tariff=tariff, year=session['year'])
            else:
                t = TariffRateCA(tariff=tariff, year=year)
            tt = None
            with open(f'/home{dev}/vector/tarifftank/app/data/ca/tarifftreatment.json', 'r') as f:
                tt = json.load(f)

            # SIMA
            sima_info = []
            with open(f'/home{dev}/vector/tarifftank/app/data/ca/sima_info.json', 'r') as f:
                sima = json.load(f)
                for row in sima:
                    if t.tariff in row['Tariff classification numbers']:
                        sima_info.append(row)
            print(sima_info)
            
            # PGA    

            return render_template('ca/tariff-lookup.html', title=t.tariff, t=t, tt=tt, sima_info=sima_info)
        except Exception as e:
            print(f"ERROR: {e}")
            flash(f"invalid 10-digit HS code - {tariff}, {e}")
    return redirect(url_for('main.index'))


# ----------CHAPTER-------------
@ca_bp.route('/<year>/chapter/<tariff>')
def chapter_lookup(year, tariff):
    chapter = tariff
    table = vars(app.ca.models)[f"CA{year}"]
    results = table.query.filter(table.tariff.like(f"{chapter}%"))
    headings = [HeadingCA(t) for t in sorted(set([i.tariff[:4] for i in results]))[:100]]

    return render_template('ca/chapter-lookup.html', headings=headings, chapter=chapter, title=f"Chapter - {chapter}")    

# ----------TEXT SEARCH-------------
@ca_bp.route('/<year>/text-search/<tariff>')
def text_search(year, tariff):
    keyword = tariff
    if ''.join(keyword.split()).isalpha():
        table = vars(app.ca.models)[f"CA{year}"]
        results = table.query.filter(table.description.like(f"%{keyword}%"))
        headings = [HeadingCA(t, year) for t in sorted(set([i.tariff[:4] for i in results]))[:100]]

        return render_template('ca/text-search.html', headings=headings, keyword=keyword, title=f"Search - {keyword}")
    else:
        return "Error"


    return render_template('ca/index.html', title="Canada", year=year, tariff=tariff)
    