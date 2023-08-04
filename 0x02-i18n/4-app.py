from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
