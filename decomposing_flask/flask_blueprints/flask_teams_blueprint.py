"""
    Blueprints provide a way to group your views into namespaces. This
    module creates  a Blueprint object which looks like a Flask app
    object, and use it to arrange a view. The main module (app.py)
    imports this file and registers its blueprint with
    app.register_blueprint(teams).
"""
from flask import Blueprint, jsonify

teams = Blueprint('teams', __name__)

_DEVS = ['Tarek', 'Syeed']
_OPS = ['Raul']
_TEAMS = {1: _DEVS, 2: _OPS}


@teams.route('/teams')
def get_all():
    return jsonify(_TEAMS)


@teams.route('/teams/<int:team_id>')
def get_team(team_id):
    return jsonify(_TEAMS[team_id])
