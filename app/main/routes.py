from flask import Blueprint, request, jsonify, render_template
from .rules import init_rules
from libs.fuzzy import Fuzzy
from libs import Topsis
from .utils import *
import numpy as np

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/calculate', methods=['POST'])
def calculate():
    alternatives = request.get_json().get('alternative')
    rules = init_rules()

    for alternative in alternatives:
        scaled_data = {
            'gaji': alternative.pop('gaji') / 1000000,
            'pengeluaran': alternative.pop('pengeluaran') / 1000000
        }

        fuzzy = Fuzzy(rules=rules, data=scaled_data)
        alternative["kondisi_ekonomi"] = fuzzy.exec()

    mapped_alternatives = map_alternative_after_fuzzied(alternatives=alternatives)

    w = np.array([0.25, 0.22, 0.15, 0.15, 0.135, 0.095])

    ct = np.array([-1, 1, 1, -1, 1, 1])

    tp = Topsis(dataset=mapped_alternatives, weight=w, criterion_type=ct)
    topsis_result, ranks_result = tp.exec()

    data = map_topsis_rank(alternatives, topsis_result, ranks_result)
    
    return jsonify({
        "status_code": 200,
        "message": 'Kalkulasi Ranking Penerima Bansos Berhasil',
        "data": convert_to_serializable(data)
    }), 200
