"""
    This module imports decomposing_flask.flask_teams_blueprint
    to regiser the team Blueprint with the main module.
"""
from flask import Flask
from decomposing_flask.flask_teams_blueprint import teams

app = Flask(__name__)

app.register_blueprint(teams)


if __name__ == "__main__":
    app.run()
