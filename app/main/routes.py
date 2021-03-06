import json
import string

from flask import (
    Blueprint, 
    render_template, 
    request, 
    redirect, 
    url_for, 
    session, 
    flash, 
    make_response, 
    jsonify
)
    
from .forms import ContactForm, SearchForm
from .models import ContactMessage
from app.factory import db
from helper_classes.heading import HeadingCA
from helper_classes.tariffrate import TariffRateCA



main_bp = Blueprint('main', __name__, url_prefix='/', template_folder='templates', static_folder='static')


@main_bp.route('/robots.txt')
def robots():
    return main_bp.send_static_file('robots.txt')

# ----------ROOT-------------
@main_bp.route('/') 
def index():
    form = SearchForm()


    return render_template('main/index.html', title="TariffTank Search", form=form)


# ----------ABOUT-------------
@main_bp.route('/about') 
def about():
    return render_template('main/about.html', title="About TariffTank(c)")


# ----------CONTACT-------------
@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():

    form = ContactForm()

    if form.validate_on_submit():
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        entry = ContactMessage(email=email, subject=subject, message=message, remote_address=request.remote_addr)
        db.session.add(entry)
        db.session.commit()


        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        flash("The form has been submitted. Thank you!")
        return redirect(url_for('main.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in the {getattr(form, field).label.text}'s field - {error}'")
        


    return render_template('main/contact.html', title='Contact', form=form)


# ----------SEARCH-------------
@main_bp.route('/search', methods=['GET', 'POST']) 
def search():
    form = SearchForm()

    
    if request.method == 'POST':
        session['year'] = request.form.get('year') or session['year']
        session['region'] = request.form.get('region') or session['region']
        keyword = request.form.get('keyword').replace('.', '')
        print(f"KEYWORD: {keyword}")

        # no input
        if not keyword:
            return redirect(url_for('main.index'))

        if len(keyword) == 2 and keyword.isdigit():
            page = 'chapter_lookup'
        elif len(keyword) in [4, 6] and keyword.isdigit():
            page = 'heading_lookup'
        elif len(keyword) == 10 and keyword.isdigit():
            page = 'tariff_lookup'
        elif ''.join(keyword.split()).isalpha():
            if len(keyword) < 3:
                flash("keyword must be minimum 4 characters")
                return redirect(url_for('main.index'))
            page = 'text_search'
        else:
            flash(f"Invalid input '{keyword}'")
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


# @main_bp.errorhandler(429)
# def ratelimit_handler(e):
#     return render_template('main/rate-limit.html', title="RATE LIMIT EXCEEDED")


    