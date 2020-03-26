from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('game', __name__)

@bp.route('/')
def index():
    return render_template('game.html')

@bp.route('/start')
def start():

    current_scene = {
    'place': 'The Village',
    'output': """
        :o-|-[
        You awaken to a sound of crumpling leaves.
        infront of you is a man waring a top hat.
        "Hello there my boy I'm sorry to awaken but this is not a charity house"
        you realise that you fell aslep out side the store.
        you apologise to the man and stand up only to get smashed into the wall by a skeloton
        what will you do?
        """
    }
    return render_template('play.html',scene=current_scene)
