from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    @app.route('/hello')
    def hello():
        return 'Hello, World'

    from . import game
    app.register_blueprint(game.bp)
    app.add_url_rule('/', endpoint='index')

    return app
