from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('game', __name__)

@bp.route('/')
def index():
    return render_template('game.html')

@bp.route('/start', methods=('GET', 'POST' ))
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
        (for the demo just skip it)
        """
    }
    if request.method == "POST":
        choice = request.form['action']
        if choice == 'skip':
            return redirect(url_for('game.campfire'))
        elif choice == 'die':
            return redirect(url_for('game.death'))
        else:
            current_scene['output']= current_scene['output'] + "what"
    return render_template('play.html',scene=current_scene)

@bp.route('/death', methods=( 'GET','POST'))
def death():
    current_scene = {
    'place':'hell',
    'output': 'GET good ... retry (You have to refresh)'
    }
    return render_template('play.html', scene=current_scene)
@bp.route('/campfire', methods=('GET','POST'))
def campfire():
    current_scene = {
    'place':'campfire',
    'output':'end of demo'
    }
    return render_template('play.html', scene=current_scene)
