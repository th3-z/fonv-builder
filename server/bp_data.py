from flask import (
    Blueprint, jsonify
)

from server.data.traits import TRAITS
from server.data.specials import SPECIALS
from server.data.skills import SKILLS
from server.data.books import BOOKS
from server.data.implants import IMPLANTS
from server.data.new_player import NEW_PLAYER
from server.data.perks import PERKS

bp = Blueprint('data', __name__, url_prefix='/')


@bp.route('/traits', methods=['GET'])
def traits():
    response_object = {'status': 'success'}
    response_object['traits'] = TRAITS
    return jsonify(response_object)

@bp.route('/specials', methods=['GET'])
def specials():
    response_object = {'status': 'success'}
    response_object['specials'] = SPECIALS
    return jsonify(response_object)

@bp.route('/skills', methods=['GET'])
def skills():
    response_object = {'status': 'success'}
    response_object['skills'] = SKILLS
    return jsonify(response_object)

@bp.route('/books', methods=['GET'])
def books():
    response_object = {'status': 'success'}
    response_object['books'] = BOOKS
    return jsonify(response_object)

@bp.route('/implants', methods=['GET'])
def implants():
    response_object = {'status': 'success'}
    response_object['implants'] = IMPLANTS
    return jsonify(response_object)

@bp.route('/perks', methods=['GET'])
def perks():
    response_object = {'status': 'success'}
    response_object['perks'] = PERKS
    return jsonify(response_object)

@bp.route('/new_player', methods=['GET'])
def new_player():
    response_object = {'status': 'success'}
    response_object['new_player'] = NEW_PLAYER
    return jsonify(response_object)
