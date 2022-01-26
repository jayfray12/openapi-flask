#!/usr/bin/env python3

import connexion
import logging

from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db = SQLAlchemy()

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://surveydb:surveydb@localhost:5432/consultant360'
    db.init_app(app.app)
    
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Feedback 360 Survey API'},
                pythonic_params=True)

    app.app.app_context().push()

    app.run(port=8080)


if __name__ == '__main__':
    main()
