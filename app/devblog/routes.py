from flask import Blueprint, render_template

devblog_bp = Blueprint('devblog', __name__, url_prefix='/devblog', template_folder='templates', static_folder='static')

@devblog_bp.route('/')
def index():
    return render_template('devblog/index.html', title='Dev Blog')


@devblog_bp.route('/<date>')
def archive(date):
    pass

#loginrequired
@devblog_bp.route('/create')
def create():
    pass

#loginrequired
@devblog_bp.route('/edit/<id>')
def edit(id):
    pass