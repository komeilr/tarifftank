from flask import Blueprint, render_template

error_bp = Blueprint('error_handlers', __name__, template_folder='templates')

@error_bp.app_errorhandler(404)
def not_found(e):
    return render_template('error_handlers/error-404.html', title="Not Found"), 404


@error_bp.app_errorhandler(429)
def rate_limit(e):
    return render_template('error_handlers/rate-limit.html', title="Rate Limit")


@error_bp.app_errorhandler(500)
def server_error(e):
    return render_template('error_handlers/server-error.html', title="Server Error"), 500