from flask import Blueprint, render_template, request
from ..database.models import get_all_data, get_subdomains

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/get_info', methods=['GET'])
def get_info():
    domain = request.args.get('domain')
    subdomains = get_subdomains(domain)  # Function to fetch data from DB
    return render_template('results.html', subdomains=subdomains)

@main_bp.route('/show_db', methods=['GET'])
def show_db():
    all_data = get_all_data()  # Function to fetch data from DB
    return render_template('show_db.html', data=all_data.to_dict(orient='records'))