from flask import Blueprint, render_template
from helper_classes.heading import HeadingCA
from helper_classes.tariffrate import TariffRateCA
import json


main_bp = Blueprint('main', __name__, url_prefix='/', template_folder='templates')

@main_bp.route('/')
def index():

    h = HeadingCA('8467')
    heading = h.gen_tariff_dict()

    #return json.dumps(heading.gen_tariff_dict())

    return render_template('main/index.html', title="Index", heading=heading)


    