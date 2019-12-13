from flask import Blueprint, render_template, request, redirect, url_for, session
from helper_classes.heading import HeadingCA
from helper_classes.tariffrate import TariffRateCA
import json


main_bp = Blueprint('main', __name__, url_prefix='/', template_folder='templates')

@main_bp.route('/')
def index():

    # h = HeadingCA('8467')
    # heading = h.gen_tariff_dict()

    #return json.dumps(heading.gen_tariff_dict())

    return render_template('main/index.html', title="Index")

@main_bp.route('/search', methods=['GET', 'POST'])
def search():
    title = "Search"

    if request.method == 'POST':
        session['year'] = request.form.get('year')
        session['region'] = request.form.get('region')
        session['keyword'] = request.form.get('keyword')
    else:
        session['year'] = '2019'
        session['region'] = 'ca'
    print(session['year'])
    print(session['region'])
    print(session['keyword'])
    return redirect(url_for('main.index'))


    