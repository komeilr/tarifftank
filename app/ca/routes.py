from flask import Blueprint, render_template

ca_bp = Blueprint('ca', __name__, url_prefix='/ca/', template_folder='templates')

@ca_bp.route('/<int:year>/<int:tariff>')
def tariff_lookup(year, tariff):
    #TODO: lookup tariff based on year
    return render_template('ca/index.html', title="Canada", tariff=tariff, year=year)
    