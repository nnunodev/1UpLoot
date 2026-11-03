import os
from os import path

import bcrypt
from bson.objectid import ObjectId
from flask import Flask, flash, redirect, render_template, request, session, url_for
from pymongo import MongoClient

if path.exists("env.py"):
    import env  # noqa: F401


class Mongo:
    """Minimal PyMongo binding replacing the unmaintained Flask-PyMongo.

    Keeps the ``mongo.db.<collection>`` call style used throughout this app.
    """

    def __init__(self, app=None):
        self.client = None
        self.db = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        uri = app.config.get("MONGO_URI")
        if not uri:
            raise RuntimeError(
                "MONGO_URI is not set — export it or create an env.py with MONGO_URI."
            )
        self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        self.db = self.client[app.config["MONGO_DBNAME"]]
        app.extensions["mongo"] = self


def create_app():
    app = Flask(__name__)

    # Secret key must exist before any session use. Read from the environment so the app
    # also works under gunicorn/Procfile, where __main__ never runs.
    app.secret_key = os.environ.get("SECRET_KEY", "dev-only-insecure-key")

    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME", "1up_loot")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    Mongo(app)
    return app


app = create_app()


def logged_in():
    return "username" in session


# route for homepage
@app.route('/')
def index():
    # Check if the user is logged in
    if logged_in():
        return render_template("index.html", user=session['username'])
    return render_template('index.html')


# route for the user to login
@app.route('/login', methods=['POST'])
def login():
    users = app.extensions["mongo"].db.users
    # find if user is in the db
    login_user = users.find_one({'name': request.form['username']})

    # if user exists compare password to db
    if login_user and bcrypt.checkpw(
        request.form['pass'].encode('utf-8'), login_user['password']
    ):
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    # same message whether or not the user exists, so an attacker can't enumerate accounts
    return render_template('login.html', error_login='Invalid username/password')


# route to login page
@app.route('/login_page')
def login_page():
    return render_template('login.html')


# route to register page
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = app.extensions["mongo"].db.users
        existing_user = users.find_one({'name': request.form['username']})
        # check if user is already registered
        if existing_user is None:
            # creates a hash for the password user typed
            hashpass = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            # adds user to database
            users.insert_one(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        # error message if the user already exists
        return render_template('register.html', error_register='Username already exists')

    return render_template('register.html')


# route to logout user.
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# user session that enables permission to edit, add, delete, search
@app.route('/<username>')
def user_games(username):
    if not logged_in():
        return redirect(url_for('index'))
    db = app.extensions["mongo"].db
    return render_template(
        "games.html",
        games=db.games.find(),
        genres=db.genres.find(),
        platforms=db.platforms.find(),
        user=session['username'],
    )


# search route for platform search
@app.route('/get_search/<search>')
def get_search(search):
    if not logged_in():
        return redirect(url_for('index'))
    db = app.extensions["mongo"].db
    plat_list = list(db.games.find({"platform_name": search}))
    return render_template(
        "results.html",
        user=session['username'],
        platforms=plat_list,
        games=db.games.find(),
        genres=db.genres.find(),
    )


# search route for game genre search
@app.route('/search_genre/<genre>')
def search_genre(genre):
    if not logged_in():
        return redirect(url_for('index'))
    db = app.extensions["mongo"].db
    genre_list = list(db.games.find({"genre_name": genre}))
    return render_template(
        "results_genre.html",
        user=session['username'],
        games=db.games.find(),
        genres=genre_list,
    )


# route for adding games page
@app.route('/add_games')
def add_games():
    if not logged_in():
        return redirect(url_for('index'))
    db = app.extensions["mongo"].db
    return render_template(
        "addgame.html",
        games=db.games.find(),
        genres=db.genres.find(),
        platforms=db.platforms.find(),
        user=session['username'],
    )


# route to add the games form data in the db.
@app.route('/insert_game', methods=['POST'])
def insert_game():
    if not logged_in():
        return redirect(url_for('index'))
    games = app.extensions["mongo"].db.games
    games.insert_one({
        'user': session['username'],
        'game_name': request.form.get('game_name'),
        'game_image': request.form.get('game_image'),
        'game_condition': request.form.get('game_condition'),
        'pickup_date': request.form.get('pickup_date'),
        'platform_name': request.form.get('platform_name'),
        'genre_name': request.form.get('genre_name'),
        'game_store': request.form.get('game_store'),
        'game_price': request.form.get('game_price'),
        'game_value': request.form.get('game_value'),
    })
    return redirect(url_for('user_games', username=session['username']))


# route to enable the user to Edit games from their list
@app.route('/edit_game/<game_id>')
def edit_game(game_id):
    if not logged_in():
        return redirect(url_for('index'))
    db = app.extensions["mongo"].db
    game_edit = db.games.find_one({"_id": ObjectId(game_id)})
    if game_edit is None:
        flash("That game is no longer in your collection.")
        return redirect(url_for('user_games', username=session['username']))
    return render_template(
        'editgame.html',
        user=session['username'],
        game=game_edit,
        genre=db.genres.find(),
        plat=db.platforms.find(),
    )


# route to update games form data in the db
@app.route('/update_game/<game_id>', methods=["POST"])
def update_game(game_id):
    if not logged_in():
        return redirect(url_for('index'))
    games = app.extensions["mongo"].db.games
    games.update_one({'_id': ObjectId(game_id)}, {'$set': {
        'user': session['username'],
        'game_name': request.form.get('game_name'),
        'game_image': request.form.get('game_image'),
        'game_condition': request.form.get('game_condition'),
        'pickup_date': request.form.get('pickup_date'),
        'platform_name': request.form.get('platform_name'),
        'genre_name': request.form.get('genre_name'),
        'game_store': request.form.get('game_store'),
        'game_price': request.form.get('game_price'),
        'game_value': request.form.get('game_value'),
    }})
    return redirect(url_for('user_games', username=session['username']))


# route to enable the user to delete the game from the db
@app.route('/delete_task/<game_id>')
def delete_game(game_id):
    if not logged_in():
        return redirect(url_for('index'))
    app.extensions["mongo"].db.games.delete_one({'_id': ObjectId(game_id)})
    return redirect(url_for('user_games', username=session['username']))


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '127.0.0.1'),
        port=int(os.environ.get('PORT', 5000)),
        debug=os.environ.get('FLASK_DEBUG') == '1',
    )
