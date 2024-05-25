from flask import Blueprint, request
from .rules import init_rules
from libs.fuzzy import Fuzzy

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return 'main index'


@main.route('/calculate', methods=['POST'])
def calculate():
    alternatives = request.get_json().get('alternative')
    rules = init_rules()

    economy_condition = []

    for alternative in alternatives:
        fuzzy = Fuzzy(rules=rules, data={
            'gaji': alternative.get('gaji') / 1000000,
            'pengeluaran': alternative.get('pengeluaran') / 1000000
        })
        economy_condition.append(fuzzy.exec())
