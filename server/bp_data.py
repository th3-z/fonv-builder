from flask import (
    Blueprint, jsonify, json
)

bp = Blueprint('data', __name__, url_prefix='/')


@bp.route('/traits', methods=['GET'])
def traits():
    response_object = {'status': 'success'}
    with open("server/data/traits.json", "r") as text_file:
        response_object['traits'] = json.load(text_file)['traits']
    return jsonify(response_object)

@bp.route('/specials', methods=['GET'])
def specials():
    response_object = {'status': 'success'}
    with open("server/data/specials.json", "r") as text_file:
        response_object['specials'] = json.load(text_file)['specials']
    return jsonify(response_object)

@bp.route('/skills', methods=['GET'])
def skills():
    response_object = {'status': 'success'}
    with open("server/data/skills.json", "r") as text_file:
        response_object['skills'] = json.load(text_file)['skills']
    return jsonify(response_object)

@bp.route('/books', methods=['GET'])
def books():
    response_object = {'status': 'success'}
    with open("server/data/books.json", "r") as text_file:
        response_object['books'] = json.load(text_file)['books']
    return jsonify(response_object)

@bp.route('/implants', methods=['GET'])
def implants():
    response_object = {'status': 'success'}
    with open("server/data/implants.json", "r") as text_file:
        response_object['implants'] = json.load(text_file)['implants']
    return jsonify(response_object)

@bp.route('/perks', methods=['GET'])
def perks():
    response_object = {'status': 'success'}
    with open("server/data/perks.json", "r") as text_file:
        response_object['perks'] = json.load(text_file)['perks']
    return jsonify(response_object)

@bp.route('/new_player', methods=['GET'])
def new_player():
    response_object = {'status': 'success'}
    with open("server/data/new_player.json", "r") as text_file:
        response_object['new_player'] = json.load(text_file)['new_player']
    return jsonify(response_object)

