from flask import Flask, jsonify


def create_app(debug=False):
    # Flask initialization and simple config
    app = Flask(__name__)
    app.debug = debug
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # Returns something for the homepage
    @app.route('/')
    def index():
        return jsonify({'message': 'Number-to-Text Converter'})

    # Sets the endpoint, attributing it to the 'converter' function
    from .converter import converter
    @app.route('/<string:num>', methods=['GET'])
    def number_converter(num):
        # Handles possible exceptions in the input
        try:
            num = int(num)
            return jsonify(converter(num))
        except ValueError:
            return jsonify({'ERROR': 'Input not an integer: cannot resolve'})

    return app
