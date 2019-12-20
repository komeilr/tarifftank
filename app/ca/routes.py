from flask import Blueprint, render_template
from helper_classes.heading import HeadingCA
from helper_classes.tariffrate import TariffRateCA

ca_bp = Blueprint('ca', __name__, url_prefix='/ca/', template_folder='templates')

@ca_bp.route('/<year>/heading/<heading>')
def heading_lookup(year, heading):
    #TODO: lookup heading based on year

    # h object contains chapter and section notes
    h = HeadingCA(heading, year)
    heading_dict = h.gen_tariff_dict()


    return render_template('ca/heading-lookup.html', title="Canada", year=year, h = h, heading_dict=heading_dict)

@ca_bp.route('/<year>/tariff/<tariff>')
def tariff_lookup(year, tariff):
    #TODO: lookup heading based on year


    return render_template('ca/index.html', title="Canada", year=year, tariff=tariff)
    