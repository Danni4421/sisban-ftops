from flask import Blueprint, request, jsonify, render_template
from .rules import init_rules
from libs.fuzzy import Fuzzy
from libs import Topsis
from ..database import db
from ..models import Fuzzy as FuzzyModel, Topsis as TopsisModel, TopsisNormalization, TopsisWeighting, TopsisBestWorst, TopsisEuclideanDistance
from .utils import *
import numpy as np

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/calculate', methods=['POST'])
def calculate():
    alternatives = request.get_json()
    rules = init_rules()

    for alternative in alternatives:
        scaled_data = {
            'penghasilan': alternative.pop('penghasilan') / 1000000,
            'pengeluaran': alternative.pop('pengeluaran') / 1000000
        }

        fuzzy = Fuzzy(rules=rules, data=scaled_data)
        (result, steps) = fuzzy.exec()
        alternative["kondisi_ekonomi"] = result
        
        for index, step in enumerate(steps):
            alternative_name = alternative.get('alternatif')

            fuzzy_entry = FuzzyModel.query.filter_by(alternative=alternative_name, rule_index=index).first()

            if fuzzy_entry is not None:
                fuzzy_entry.alpha_v1 = step.get('alpha_s')[0]
                fuzzy_entry.alpha_v2 = step.get('alpha_s')[1]
                fuzzy_entry.alpha = step.get('alpha_pred')
                fuzzy_entry.z_result = step.get('z_pred')
                fuzzy_entry.a_pred_multiply_z_pred = step.get('a_pred_multiply_z_pred')
            else:
                fuzzy_model = FuzzyModel(
                    alternative=alternative_name,
                    rule_index=index,
                    alpha_v1=step.get('alpha_s')[0],
                    alpha_v2=step.get('alpha_s')[1],
                    alpha=step.get('alpha_pred'),
                    z_result=step.get('z_pred'),
                    a_pred_multiply_z_pred=step.get('a_pred_multiply_z_pred')
                )
                db.session.add(fuzzy_model)
            
        db.session.commit()

    mapped_alternatives = map_alternative_after_fuzzied(alternatives=alternatives)

    w = np.array([0.25, 0.22, 0.15, 0.15, 0.135, 0.095])

    ct = np.array([-1, 1, 1, -1, 1, 1])

    tp = Topsis(
        alternatives=[alternative.get('alternatif') for alternative in alternatives], 
        dataset=mapped_alternatives, 
        weight=w, 
        criterion_type=ct
    )
    topsis_result, ranks_result = tp.exec()

    data = map_topsis_rank(alternatives, topsis_result, ranks_result)
    
    return jsonify({
        "status_code": 200,
        "message": 'Kalkulasi Ranking Penerima Bansos Berhasil',
        "data": convert_to_serializable(data)
    }), 200


@main.route('/fuzzy/<alternative>', methods=['GET'])
def get_fuzzy_calculation(alternative):
    fuzzy_calculations = FuzzyModel.query.filter_by(alternative=alternative).all()

    if not fuzzy_calculations:
        return jsonify({
            "status_code": 200,
            "message": 'Gagal mendapatkan hasil perhitungan fuzzy, Kalkulasi alternatif tidak ditemukan',
            "data": None
        })

    data = [fuzzy.to_dict() for fuzzy in fuzzy_calculations]

    return jsonify({
        "status_code": 200,
        "message": 'Berhasil mendapatkan hasil kalkulasi fuzzy',
        "data": data
    })


@main.route('/topsis', methods=['GET'])
def get_topsis_calculation():
    topsis = TopsisModel.query.all()
    topsis_normalization = TopsisNormalization.query.all()
    topsis_weighting = TopsisWeighting.query.all()
    topsis_best_worst = TopsisBestWorst.query.all()
    topsis_euclidean = TopsisEuclideanDistance.query.all()

    return jsonify({
        "status_code": 200,
        "message": "Berhasil mendapatkan hasil kalkulasi Topsis",
        "data": {
            "evaluation_matrix": [t.to_dict() for t in topsis],
            "normalization": [tn.to_dict() for tn in topsis_normalization],
            "weighting": [tw.to_dict() for tw in topsis_weighting],
            "best_worst_alternative": [bw.to_dict() for bw in topsis_best_worst],
            "euclidean": [te.to_dict() for te in topsis_euclidean]
        }
    })