import os

from flask import Flask, jsonify, request
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'store.sqlite'),
    )
    
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass
    
    from . import bp_data
    app.register_blueprint(bp_data.bp)

    from . import db
    db.init_app(app)
    
    return app
