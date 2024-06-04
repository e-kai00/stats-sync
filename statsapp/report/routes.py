from flask import Blueprint


report = Blueprint('report', __name__)

@report.route('/report')
def generate_report():
    return '<h1>Here will be report</h1>'