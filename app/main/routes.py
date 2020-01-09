from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response, jsonify
from helper_classes.heading import HeadingCA
from helper_classes.tariffrate import TariffRateCA
import json
import string


main_bp = Blueprint('main', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@main_bp.route('/robots.txt')
def robots():
    return main_bp.send_static_file('robots.txt')

@main_bp.route('/')
def index():

    # h = HeadingCA('8467')
    # heading = h.gen_tariff_dict()

    #return json.dumps(heading.gen_tariff_dict())

    return render_template('main/index.html', title="TariffTank Search")


@main_bp.route('/about')
def about():

    return render_template('main/about.html', title="About TariffTank(c)")

@main_bp.route('/search', methods=['GET', 'POST'])
def search():    

    if request.method == 'POST':
        session['year'] = request.form.get('year')
        session['region'] = request.form.get('region')
        keyword = request.form.get('keyword').replace('.', '')
        print(len(keyword))

        # no input
        if not keyword:
            return redirect(url_for('main.index'))

        if len(keyword) == 2 and keyword.isdigit():
            page = 'chapter_lookup'
        elif len(keyword) == 4 and keyword.isdigit():
            page = 'heading_lookup'
        elif len(keyword) == 10 and keyword.isdigit():
            page = 'tariff_lookup'
        elif ''.join(keyword.split()).isalpha():
            if len(keyword) < 4:
                flash("keyword must be minimum 4 characters")
                return redirect(url_for('main.index'))
            page = 'text_search'
        else:
            flash("Invalid input")
            return redirect(url_for('main.index'))
        

        if session['region'] == 'ca':
            return redirect(url_for(f'ca.{page}', year=session['year'], tariff=keyword))

        # elif session['region'] == 'us':
        #     return redirect(url_for(f'us.{page}', year=session['year'], tariff=keyword))

        # elif session['region'] == 'eu':
        #     return redirect(url_for(f'eu.{page}', year=session['year'], tariff=keyword))

    else:
        session['year'] = '2020'
        session['region'] = 'ca'
    print(session['year'])
    print(session['region'])
    
    return redirect(url_for('main.index'))


@main_bp.errorhandler(429)
def ratelimit_handler(e):
    return render_template('main/rate-limit.html', title="RATE LIMIT EXCEEDED")


    