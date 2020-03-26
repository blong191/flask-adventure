from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('game', __name__)

@bp.route('/')
def index():
    return render_template('game.html')

@bp.route('/start')
def start():
    return render_template('play.html')
