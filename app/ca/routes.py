import csv
import json

from flask import Blueprint, render_template, redirect, url_for, flash
from helper_classes.heading import HeadingCA
from helper_classes.tariffrate import TariffRateCA

ca_bp = Blueprint('ca', __name__, url_prefix='/ca/', template_folder='templates')

@ca_bp.route('/<year>/heading/<tariff>')
def heading_lookup(year, tariff):
    #TODO: add PGA stats

    # h object contains chapter and section notes
    if len(tariff) == 4:
        try:
            h = HeadingCA(tariff, year)
            heading_dict = h.gen_tariff_dict()
            return render_template('ca/heading-lookup.html', title="Canada", year=year, h=h)
        except:
            flash(f"Invalid heading {tariff}")
    else:
        flash(f"Invalid tariff {tariff}")
    return redirect(url_for('main.index'))


@ca_bp.route('/<year>/tariff/<tariff>')
def tariff_lookup(year, tariff):
    #TODO: lookup tariff
    #TODO: include s/ch notes and pga
    if len(tariff) == 10:
        try:
            t = TariffRateCA(tariff=tariff, year=year)
            tt = None
            with open('app/data/ca/tarifftreatment.json') as f:
                tt = json.load(f)
            
            # PGA    

            return render_template('ca/tariff-lookup.html', title="Tariff Rates", t=t, tt=tt)
        except:
            flash(f"invalid 10-digit HS code - {tariff}")
    return redirect(url_for('main.index'))


@ca_bp.route('/text-search/<year>/<tariff>')
def text_search(year, tariff):
    keyword = str(tariff)
    if keyword.isalpha():
        return f"<h1>{keyword}</h1>"
    else:
        return "Error"


    return render_template('ca/index.html', title="Canada", year=year, tariff=tariff)
    