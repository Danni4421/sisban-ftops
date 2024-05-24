from flask import Blueprint, request

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return 'main index'


@main.route('/calculate', methods=['POST'])
def calculate():
    return 'for calculating'
