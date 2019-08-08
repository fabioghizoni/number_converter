from flask import Flask

def create_app(debug = False):
    # Flask initialization and simple config
    app = Flask(__name__)
    app.debug = debug
    app.config.from_mapping(
        SECRET_KEY = 'dev',
    )

    # Returns something for the homepage
    @app.route('/')
    def index():
        return 'TESTE'

    return app
