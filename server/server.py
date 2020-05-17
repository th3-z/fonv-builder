import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from data.traits import TRAITS
from data.specials import SPECIALS
from data.skills import SKILLS

# configuration
DEBUG = True
PORT = 8081

server = Flask(__name__)
server.config.from_object(__name__)

# enable CORS
CORS(server, resources={r'/*': {'origins': '*'}})

@server.route('/traits', methods=['GET'])
def traits():
    response_object = {'status': 'success'}
    response_object['traits'] = TRAITS
    return jsonify(response_object)

@server.route('/specials', methods=['GET'])
def specials():
    response_object = {'status': 'success'}
    response_object['specials'] = SPECIALS
    return jsonify(response_object)

@server.route('/skills', methods=['GET'])
def skills():
    response_object = {'status': 'success'}
    response_object['skills'] = SKILLS
    return jsonify(response_object)

if __name__ == '__main__':
    server.run(port=PORT)
